<template>
  <div class="publications-container">
    <div class="view-header-title">
        <h1 >Research Publications</h1 >
        <p class="subheading">Showcasing my academic work and research contributions.</p>
    </div>
    <!-- Publication 1: arXiv -->
    <section class="publication-card">
      <header class="publication-header">
        <a href="https://arxiv.org/abs/2501.14739" target="_blank" class="publication-title">
          Reproduction Research of FSA-Benchmark (arXiv:2501.14739)
        </a>
      </header>
      <div class="publication-meta">
        <div class="meta-item">
          <span class="meta-label">Subject:</span >
          <span class="meta-value">Distributed, Parallel, and Cluster Computing</span>
        </div>
        <div class="meta-item">
          <span class="meta-label">Source:</span >
          <a href="https://arxiv.org/abs/2501.14739" target="_blank" class="meta-value-link">arXiv</a>
        </div>
      </div>
      <p class="summary-text">This research focuses on the reliability and performance of storage systems, specifically addressing the challenge of detecting fail-slow disks. It proposes a hybrid deep learning framework combining convolutional-recurrent layers with self-attention mechanisms to model complex temporal dependencies in disk metrics.</p>
    </section>
    <div class="divider"></div>
    <!-- Publication 2: eEngrXiv -->
    <section class="publication-card">
      <header class="publication-header">
        <a href="https://engrxiv.org/preprint/view/6177" target="_blank" class="publication-title">
          Hybrid Deep Learning for Fail Slow Disk Detection in the FSA Benchmark (eEngrXiv:6177)
        </a>
      </header>
      <div class="publication-meta">
        <div class="meta-item">
          <span class="meta-label">Subject:</span >
          <span class="meta-value">Deep Learning, defect detection</span>
        </div>
        <div class="meta-item">
          <span class="meta-label">Source:</span >
          <a href="https://engrxiv.org/preprint/view/6177" target="_blank" class="meta-value-link">eEngrXiv</a>
        </div>
      </div>
      <p class="summary-text">This work builds upon the FSA-benchmark dataset (PERSEUS) to detect fail-slow conditions. It proposes a hybrid deep learning framework that integrates transformer-based mechanisms to better capture long-range dependencies in disk performance data, showing promising results in preliminary experiments.</p>
    </section>
  </div >
</template>
<script setup>
// No script logic needed for now, just displaying static content.
</script>
<style scoped>
/* Publications Header - Matches .about-header and .contact-header styling */
.view-header-title {
    text-align: center;
    margin-bottom: 3.5rem;
    max-width: 1000px;
    margin-left: auto;
    margin-right: auto;
    padding: 3rem 2.5rem;
    background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
    border-radius: var(--radius-xl);
    color: var(--white-color);
    box-shadow: var(--shadow-primary);
    position: relative;
    overflow: hidden;
}

.view-header-title::before {
    content: '';
    position: absolute;
    inset: 0;
    background: radial-gradient(ellipse 80% 80% at 50% 50%, rgba(255,255,255,0.1) 0%, transparent 70%);
    pointer-events: none;
}

/* Main Title styling */
.view-header-title h1 {
    color: var(--white-color);
    margin-bottom: 1rem;
    font-weight: 900;
    position: relative;
    z-index: 1;
    background: none !important;
    -webkit-background-clip: unset !important;
    -webkit-text-fill-color: var(--white-color) !important;
}

.view-header-title .subheading {
    font-size: 1.05rem;
    color: rgba(255,255,255,0.8);
    max-width: 750px;
    margin: 0 auto;
    line-height: 1.8;
    position: relative;
    z-index: 1;
}
/* Individual Card Styling */
.publication-card {
  background-color: #ffffff;
  border: 1px solid #e0e0e0;
  border-radius: 12px;
  padding: 30px;
  margin-bottom: 30px;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.08);
  transition: transform 0.3s ease-out, box-shadow 0.3s ease-out;
}
.publication-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.12);
}
/* Header/Title Styling */
.publication-header {
  margin-bottom: 15px;
}
.publication-title {
  font-size: 1.9em;
  color: #1e40af; /* Deep blue for prominence */
  text-decoration: none;
  display: block;
  margin-bottom: 10px;
}
.publication-title:hover {
  color: #0056b3;
  text-decoration: underline;
}
/* Metadata and Summary */
.publication-meta {
  display: flex;
  flex-wrap: wrap;
  gap: 25px;
  padding-bottom: 15px;
  border-bottom: 1px solid #eee;
  margin-bottom: 25px;
}
.meta-item {
  display: flex;
  flex-direction: column;
}
.meta-label {
  font-weight: 600;
  color: #777;
  margin-bottom: 4px;
  font-size: 0.9em;
  text-transform: uppercase;
  letter-spacing: 0.02em;
}
.meta-value, .meta-value-link {
  font-size: 1em;
  color: #444;
}
.meta-value-link {
    color: #4f46e5; /* Use primary blue from header */
    text-decoration: none;
}
.meta-value-link:hover {
    text-decoration: underline;
}
.summary-text {
  font-size: 1.1em;
  line-height: 1.7;
  color: #333;
  border-left: 4px solid #4f46e5;
  padding-left: 20px;
  margin-top: 20px;
}
/* Divider for visual separation */
.divider {
  height: 1px;
  background-color: #e0e0e0;
  margin: 40px 0;
}
</style>