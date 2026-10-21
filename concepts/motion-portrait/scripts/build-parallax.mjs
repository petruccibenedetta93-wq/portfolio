// Builds the PARALLAX draft from parallax/src: the twelve ring paths are injected verbatim
// from rings.paths.txt and checked again in the output.
//   node scripts/build-parallax.mjs                 -> parallax/index.html (repository paths)
//   node scripts/build-parallax.mjs standalone      -> standalone/benedetta-parallax.html (photo inlined)
//   node scripts/build-parallax.mjs artifact <dir>  -> <dir>/parallax/ (links to the live site)
import { copyFileSync, mkdirSync, readFileSync, writeFileSync } from 'node:fs'
import { join, resolve } from 'node:path'

const here = resolve(import.meta.dirname, '..')
const LIVE_SITE = 'https://petruccibenedetta93-wq.github.io/portfolio/'
const src = join(here, 'parallax/src')
const photo = join(here, 'parallax/assets/benedetta-16x9.jpg')

const paths = readFileSync(join(src, 'rings.paths.txt'), 'utf8').split('\n').filter(Boolean)
if (paths.length !== 12) throw new Error(`rings.paths.txt has ${paths.length} paths, expected 12`)

const word = (w) => `<span class="word">${[...w].map((c) => `<span aria-hidden="true">${c}</span>`).join('')}</span>`

function render(root, img) {
  return readFileSync(join(src, 'template.html'), 'utf8')
    .replace('__RINGS__', paths.map((d) => `      <path d="${d}"/>`).join('\n'))
    .replace('__TITLE__', word('BENEDETTA') + word('PETRUCCI'))
    .replaceAll('__ROOT__', root)
    .replace('__IMG__', img)
}

function check(html, label) {
  const found = [...html.matchAll(/<path d="([^"]*)"\/>/g)].map((m) => m[1])
  if (found.length !== 12 || found.some((d, i) => d !== paths[i])) throw new Error(`${label}: ring paths differ from rings.paths.txt`)
  if (/href="#"/.test(html)) throw new Error(`${label}: contains href="#"`)
  console.log(`${label}: 12 ring paths identical, ${(html.length / 1024).toFixed(0)} KB`)
}

const [mode = 'repo', dir] = process.argv.slice(2)
if (mode === 'repo') {
  const html = render('../../../', 'assets/benedetta-16x9.jpg')
  check(html, 'parallax/index.html')
  writeFileSync(join(here, 'parallax/index.html'), html)
} else if (mode === 'standalone') {
  const html = render(LIVE_SITE, `data:image/jpeg;base64,${readFileSync(photo).toString('base64')}`)
  check(html, 'standalone/benedetta-parallax.html')
  mkdirSync(join(here, 'standalone'), { recursive: true })
  writeFileSync(join(here, 'standalone/benedetta-parallax.html'), html)
} else if (mode === 'artifact' && dir) {
  const out = join(resolve(dir), 'parallax')
  mkdirSync(join(out, 'assets'), { recursive: true })
  const html = render(LIVE_SITE, 'assets/benedetta-16x9.jpg')
  check(html, 'artifact parallax/index.html')
  writeFileSync(join(out, 'index.html'), html)
  copyFileSync(photo, join(out, 'assets/benedetta-16x9.jpg'))
} else {
  throw new Error('usage: build-parallax.mjs [repo | standalone | artifact <dir>]')
}
