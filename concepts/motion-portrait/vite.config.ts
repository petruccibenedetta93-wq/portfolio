import { resolve } from 'node:path'
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// Live site: used only in dev and for the private Claude preview (artifact mode),
// where the repository pages are not served next to the concept.
const LIVE_SITE = 'https://petruccibenedetta93-wq.github.io/portfolio/'

export default defineConfig(({ command, mode }) => {
  // Repository build: preview/a/index.html -> ../../../../ is the portfolio root.
  const siteRoot = command === 'build' && mode !== 'artifact' ? '../../../../' : LIVE_SITE
  // The private preview carries its own copy of the portrait; the repository build reuses the original file.
  const portrait = mode === 'artifact' ? '../benedetta-cutout-hq.png' : `${siteRoot}assets/images/benedetta-cutout-hq.png`
  const outDir = mode === 'artifact' ? resolve(process.env.ARTIFACT_OUT ?? 'artifact-build') : resolve(__dirname, 'preview')

  return {
    root: resolve(__dirname, 'app'),
    base: './',
    publicDir: false,
    plugins: [react()],
    define: { __SITE_ROOT__: JSON.stringify(siteRoot), __PORTRAIT__: JSON.stringify(portrait) },
    build: {
      outDir,
      emptyOutDir: true,
      rollupOptions: {
        input: {
          index: resolve(__dirname, 'app/index.html'),
          a: resolve(__dirname, 'app/a/index.html'),
          b: resolve(__dirname, 'app/b/index.html'),
        },
      },
    },
  }
})
