// Builds one self-contained HTML file per variant (JS, CSS and portrait inlined) that opens
// straight from the file system with a double click. Links point to the live portfolio pages.
import { execFileSync } from 'node:child_process'
import { mkdirSync, readFileSync, rmSync, writeFileSync } from 'node:fs'
import { tmpdir } from 'node:os'
import { join, resolve } from 'node:path'
import { build } from 'esbuild'

const here = resolve(import.meta.dirname, '..')
const LIVE_SITE = 'https://petruccibenedetta93-wq.github.io/portfolio/'
// The original portrait from the repository, embedded unchanged.
const portraitFile = resolve(here, '../../assets/images/benedetta-cutout-hq.png')
const portrait = `data:image/png;base64,${readFileSync(portraitFile).toString('base64')}`
const outDir = join(here, 'standalone')
const tmp = join(tmpdir(), 'bp-standalone')
mkdirSync(outDir, { recursive: true })
mkdirSync(tmp, { recursive: true })

const variants = [
  { id: 'a', file: 'variante-a-motion-portrait.html' },
  { id: 'b', file: 'variante-b-editorial-portrait.html' },
]

for (const v of variants) {
  const cssOut = join(tmp, `${v.id}.css`)
  execFileSync(join(here, 'node_modules/.bin/tailwindcss'), ['-c', join(here, 'tailwind.config.ts'), '-i', join(here, `src/variant-${v.id}/${v.id}.css`), '-o', cssOut, '--minify'], { cwd: here, stdio: 'pipe' })
  const css = readFileSync(cssOut, 'utf8')

  const result = await build({
    entryPoints: [join(here, `src/variant-${v.id}/main.tsx`)],
    bundle: true,
    format: 'iife',
    minify: true,
    write: false,
    jsx: 'automatic',
    loader: { '.css': 'empty' },
    define: {
      __SITE_ROOT__: JSON.stringify(LIVE_SITE),
      __PORTRAIT__: JSON.stringify(portrait),
      'process.env.NODE_ENV': '"production"',
    },
  })
  const js = result.outputFiles[0].text.replaceAll('</script', '<\\/script')

  const html = readFileSync(join(here, `app/${v.id}/index.html`), 'utf8')
    .replace(/\s*<script type="module"[^>]*><\/script>/, '')
    .replace('</head>', `    <style>${css}</style>\n  </head>`)
    .replace('</body>', `    <script>${js}</script>\n  </body>`)
  writeFileSync(join(outDir, v.file), html)
  console.log(`${v.file}  ${(html.length / 1024).toFixed(0)} KB`)
}
rmSync(tmp, { recursive: true, force: true })
