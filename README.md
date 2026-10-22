# Joshua Ludolf Portfolio - Vue.js Version

This is a Vue.js single-page application (SPA) version of Joshua Ludolf's portfolio website, converted from the original static HTML files.

## Features

✅ **Responsive Design** - Works on all device sizes  
✅ **Vue Router** - Client-side navigation between pages  
✅ **Reactive Components** - Dynamic content and forms  
✅ **Modern Vue 3** - Using Composition API and `<script setup>`  
✅ **Vite Build System** - Fast development and optimized production builds

## Pages

- **Home** (`/`) - Portfolio introduction with education cards and hero section
- **About** (`/about`) - Technical skills, experience, and educational background  
- **Projects** (`/projects`) - Showcase of development projects with links to GitHub
- **Contact** (`/contact`) - Contact form with multiple email options and social links
- **Privacy Policy** (`/privacy`) - Privacy policy and data protection information
- **Terms of Service** (`/terms`) - Website terms and conditions

## Development

### Prerequisites
- Node.js 20.19.0+ or 22.12.0+
- npm or yarn package manager

### Getting Started

1. **Navigate to the vue-project directory:**
   ```bash
   cd vue-project
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Start the development server:**
   ```bash
   npm run dev
   ```
   This starts both Vite and the local OpenRouter avatar API. The API key stays in
   `avatar-agent/.env` and is never sent to the browser.
   The dev launcher also starts the LiveKit/Synthesia worker so the avatar can join
   the room and publish its lip-synced video. Allow microphone access in the browser,
   then speak to the avatar. Typed questions are sent over LiveKit to the worker;
   OpenRouter generates the response there, NVIDIA Magpie Multilingual supplies
   the speech audio, and Synthesia speaks/lip-syncs it. The agent requires an
   `NVIDIA_API_KEY` in `avatar-agent/.env`.
   For local setup, copy `avatar-agent/.env.example` to `avatar-agent/.env`
   and fill in the LiveKit, Synthesia, OpenRouter, and NVIDIA credentials.

4. **Open your browser:**
   - The application will be available at `http://localhost:5173` (or the next available port)
   - Vue DevTools will be available at the devtools URL shown in the terminal

### Available Scripts

- `npm run dev` - Start Vite and the local avatar API with hot reload
- `npm run dev:frontend` - Start only the Vite frontend
- `npm run dev:avatar` - Start only the local OpenRouter avatar API
- `npm run build` - Build for production  
- `npm run preview` - Preview production build locally

Set `AVATAR_AUTOSTART_AGENT=false` when you want to run the frontend and token API
without starting the LiveKit worker.

### Public live avatar deployment

GitHub Pages hosts only the Vue frontend. The LiveKit token API and Synthesia
worker run on Railway from the `avatar-agent` directory.

1. Create a Railway service using the repository's `avatar-agent` directory.
  Use `avatar-agent/Dockerfile` (or set the service root directory to
  `avatar-agent`) and expose the service's generated public URL.
2. In Railway's **Variables** page, enter these six values from
  `avatar-agent/.env`: `OPENROUTER_API_KEY`, `NVIDIA_API_KEY`, `LIVEKIT_URL`,
  `LIVEKIT_API_KEY`, `LIVEKIT_API_SECRET`, and `SYNTHESIA_API_KEY`.
  Never commit these values or put them in the Pages build.
3. The production frontend uses
  `https://joshua-ludolf-avatar-production.up.railway.app/api/token` by
  default. If Railway assigns a different public URL, set that complete
  `/api/token` URL as the GitHub repository secret
  `VITE_AVATAR_TOKEN_ENDPOINT` under **Settings → Secrets and variables →
  Actions**, then redeploy the Pages site.
4. Open the site in a new/private browser window. The Railway service's
  `/health` endpoint should return `{"status":"ok"}` and the avatar should
  connect after microphone permission is granted.

If `/health` is unavailable, inspect the Railway deployment logs and confirm
the service is listening on Railway's `PORT` value before testing the frontend.

## Project Setup

```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Compile and Minify for Production

```sh
npm run build
```
