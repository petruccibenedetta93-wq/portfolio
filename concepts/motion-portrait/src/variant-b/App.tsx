import { ArrowRight, Menu, X } from 'lucide-react'
import { Monogram } from '../shared/Monogram'
import { PortraitMedia } from '../shared/PortraitMedia'
import { site } from '../shared/site'
import { useMenu } from '../shared/useMenu'
import { usePointerDrift } from '../shared/usePointerDrift'

const links = [
  { label: 'Progetti', href: site.projects },
  { label: 'Profilo', href: site.profile },
  { label: 'Contatti', href: site.contacts },
]
const pills = ['UX/UI Design', 'Visual storytelling', 'Comunicazione']

const glass = 'border border-white/10 bg-black/25 backdrop-blur-md'

export default function App() {
  const menu = useMenu({ closeAbove: '(min-width: 768px)', trapTrigger: true })
  const driftRef = usePointerDrift<HTMLDivElement>(10)

  return (
    <div className="relative min-h-[100svh] w-full overflow-x-clip bg-[#14181c] text-white">
      {/* Media: studio-backdrop tone, portrait, and a functional low scrim for the copy */}
      <div aria-hidden="true" className="absolute inset-0 bg-[radial-gradient(ellipse_70%_60%_at_56%_30%,#56616c_0%,#2f373f_48%,#14181c_100%)] md:bg-[radial-gradient(ellipse_60%_70%_at_64%_32%,#56616c_0%,#2f373f_48%,#14181c_100%)] lg:bg-[radial-gradient(ellipse_55%_75%_at_62%_30%,#56616c_0%,#2f373f_50%,#14181c_100%)]" />
      <div className="pointer-events-none absolute inset-0 overflow-hidden">
        <div ref={driftRef} className="absolute inset-0 will-change-transform">
          <PortraitMedia className="b-portrait absolute top-[4svh] h-[100svh] w-auto sm:min-h-full max-w-none select-none [filter:saturate(0.9)_contrast(1.04)] sm:top-[6svh] desk:top-[5svh] desk:h-[112svh]" />
        </div>
        <div aria-hidden="true" className="absolute inset-x-0 bottom-0 h-[58%] bg-gradient-to-t from-[#0d1013] via-[#0d1013]/75 to-transparent" />
      </div>

      <div className="relative z-10 flex min-h-[100svh] flex-col px-4 py-4 sm:px-10 sm:py-8 lg:px-12">
        {/* Navigation */}
        <header className="relative flex items-center justify-between gap-3">
          <div className="flex items-center gap-2">
            <a href={site.home} className={`press flex items-center gap-3 rounded-2xl px-4 py-2.5 hover:bg-black/35 sm:px-6 sm:py-4 ${glass}`}>
              <Monogram className="h-5 w-5 sm:h-7 sm:w-7" />
              <span className="font-serif text-base font-light tracking-wide sm:text-xl">Benedetta Petrucci</span>
            </a>
            <nav aria-label="Navigazione principale" className={`hidden rounded-2xl md:block ${glass}`}>
              <ul className="flex items-center px-2 text-sm">
                {links.map((l) => (
                  <li key={l.label}>
                    <a href={l.href} className="press inline-flex min-h-11 items-center rounded-xl px-4 py-3 text-white/85 hover:bg-white/10 hover:text-white sm:py-[1.05rem]">
                      {l.label}
                    </a>
                  </li>
                ))}
              </ul>
            </nav>
          </div>

          <div className="flex items-center gap-2">
            <a href={site.contacts} className="press hidden rounded-full bg-white px-6 py-3 text-sm font-medium text-gray-900 hover:bg-white/90 sm:inline-flex">
              Contattami
            </a>
            <button
              ref={menu.triggerRef}
              type="button"
              className={`press inline-flex h-11 w-11 items-center justify-center rounded-2xl md:hidden ${glass}`}
              aria-label={menu.open ? 'Chiudi il menu' : 'Apri il menu'}
              aria-expanded={menu.open}
              aria-controls="menu-b"
              onClick={menu.toggle}
            >
              {menu.open ? <X size={20} strokeWidth={1.5} aria-hidden="true" /> : <Menu size={20} strokeWidth={1.5} aria-hidden="true" />}
            </button>
          </div>

          <div
            id="menu-b"
            ref={menu.panelRef}
            data-open={menu.open}
            className="menu-b absolute left-0 right-0 top-[4.5rem] rounded-2xl border border-white/10 bg-black/40 p-5 backdrop-blur-xl md:hidden"
          >
            <nav aria-label="Navigazione mobile">
              <ul className="flex flex-col">
                {links.map((l) => (
                  <li key={l.label}>
                    <a href={l.href} onClick={menu.close} className="press flex min-h-12 items-center font-serif text-2xl font-light">
                      {l.label}
                    </a>
                  </li>
                ))}
              </ul>
              <a href={site.cv} onClick={menu.close} className="press mt-4 flex min-h-12 items-center justify-center rounded-full bg-white px-6 text-sm font-medium text-gray-900">
                Vedi il CV
              </a>
            </nav>
          </div>
        </header>

        {/* Mobile spacer keeps the face clear of the copy */}
        <div className="min-h-[calc(48svh-3rem)] flex-1 sm:min-h-0" />

        <main inert={menu.open} className="flex flex-col pb-4 sm:mt-auto sm:pt-10 sm:flex-row sm:items-end sm:justify-between sm:gap-10 sm:pb-12 lg:pb-16">
          <div className="max-w-[700px]">
            <h1 className="font-serif text-[2.5rem] font-light leading-[1.05] tracking-tight sm:text-[3.5rem] md:text-[4.5rem] lg:text-[5.5rem] [@media(max-height:560px)]:text-[2.75rem]">
              Idee che prendono forma.
            </h1>
            <p className="mt-4 max-w-[520px] text-sm leading-relaxed text-white/80 sm:mt-6 sm:text-base md:text-lg">
              Sono Benedetta, UX/UI designer con un background in comunicazione e visual design. Progetto interfacce chiare e identità riconoscibili.
            </p>

            <div className={`mt-6 flex w-full max-w-[520px] items-center justify-between gap-2 rounded-full p-1.5 sm:mt-8 ${glass}`}>
              <a href={site.projects} className="press inline-flex min-h-12 flex-1 items-center justify-center gap-2 whitespace-nowrap rounded-full bg-white px-4 min-[360px]:px-5 text-sm font-medium text-gray-900 hover:bg-white/90 sm:flex-none sm:px-7">
                Esplora i progetti
                <ArrowRight size={16} aria-hidden="true" />
              </a>
              <a href={site.cv} className="press inline-flex min-h-12 items-center justify-center whitespace-nowrap rounded-full px-4 text-sm font-medium text-white hover:bg-white/10 min-[360px]:px-5 sm:px-7">
                Vedi il CV
              </a>
            </div>

            <ul className="mt-4 flex flex-wrap gap-2 sm:hidden" aria-label="Ambiti">
              {pills.map((p) => (
                <li key={p} className="rounded-full border border-white/10 bg-black/30 px-3 py-1.5 text-xs backdrop-blur-md">
                  {p}
                </li>
              ))}
            </ul>
          </div>

          <ul className="hidden flex-col items-end gap-2 self-end sm:flex" aria-label="Ambiti">
            {pills.map((p) => (
              <li key={p} className="whitespace-nowrap rounded-full border border-white/10 bg-black/30 px-4 py-2 text-xs backdrop-blur-md sm:text-sm">
                {p}
              </li>
            ))}
          </ul>
        </main>
      </div>
    </div>
  )
}
