import { spawn } from 'node:child_process'
import { createConnection } from 'node:net'
import { existsSync } from 'node:fs'
import { resolve } from 'node:path'
import { fileURLToPath } from 'node:url'

const root = resolve(fileURLToPath(new URL('..', import.meta.url)))
const apiPort = Number(process.env.AVATAR_CHAT_PORT || 8787)
const viteBin = resolve(root, 'node_modules', 'vite', 'bin', 'vite.js')
const apiRoot = resolve(root, 'avatar-agent')
const apiScript = resolve(root, 'avatar-agent', 'chat_api.py')
const agentScript = resolve(root, 'avatar-agent', 'agent.py')
const forwardedArgs = process.argv.slice(2)

if (!existsSync(apiScript)) {
  console.error(`Missing avatar API script: ${apiScript}`)
  process.exit(1)
}

const canConnect = () => new Promise((resolveConnection) => {
  const socket = createConnection({ host: '127.0.0.1', port: apiPort })
  socket.once('connect', () => {
    socket.destroy()
    resolveConnection(true)
  })
  socket.once('error', () => resolveConnection(false))
})

const waitForApi = async (attempts = 30) => {
  for (let attempt = 0; attempt < attempts; attempt += 1) {
    if (await canConnect()) return true
    await new Promise((resolveDelay) => setTimeout(resolveDelay, 250))
  }
  return false
}

const startApi = () => {
  const command = process.env.AVATAR_PYTHON
    ? { executable: process.env.AVATAR_PYTHON, args: [apiScript] }
    : { executable: 'uv', args: ['run', '--project', apiRoot, 'python', 'chat_api.py'] }

  return spawn(command.executable, command.args, {
    cwd: apiRoot,
    stdio: 'inherit',
    windowsHide: true
  })
}

const startAgent = () => spawn('uv', ['run', '--project', apiRoot, 'python', agentScript, 'dev'], {
  cwd: apiRoot,
  stdio: 'inherit',
  windowsHide: true
})

const apiAlreadyRunning = await canConnect()
const apiProcess = apiAlreadyRunning ? null : startApi()

if (!apiAlreadyRunning && !(await waitForApi())) {
  apiProcess?.kill()
  console.error(`Avatar API did not start on http://127.0.0.1:${apiPort}.`)
  console.error('Install uv or set AVATAR_PYTHON to a Python executable with avatar-agent dependencies.')
  process.exit(1)
}

const agentProcess = process.env.AVATAR_AUTOSTART_AGENT === 'false' ? null : startAgent()

const viteProcess = spawn(process.execPath, [viteBin, ...forwardedArgs], {
  cwd: root,
  stdio: 'inherit',
  windowsHide: true
})

const shutdown = () => {
  viteProcess.kill()
  apiProcess?.kill()
  agentProcess?.kill()
}

process.on('SIGINT', shutdown)
process.on('SIGTERM', shutdown)
viteProcess.on('exit', (code, signal) => {
  apiProcess?.kill()
  agentProcess?.kill()
  process.exit(code ?? (signal ? 1 : 0))
})
