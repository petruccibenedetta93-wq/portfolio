import { useEffect } from 'react'
import { ArrowUpRight, Menu, X } from 'lucide-react'
import { Monogram } from '../shared/Monogram'
import { PortraitMedia } from '../shared/PortraitMedia'
import { navItems, site } from '../shared/site'
import { useMenu } from '../shared/useMenu'
import { usePointerDrift } from '../shared/usePointerDrift'

const skills = ['UX research e test', 'Wireframe e prototipi', 'UI e design system', 'Visual identity', 'Video e contenuti']
const chips = ['UX/UI Design', 'Visual Design', 'Video']

// Rendered once per layout: above the portrait in the scrolling layout, beside the title on desktop.
function Actions({ className = '' }: { className?: string }) {
  return (
    <div className={`flex-wrap items-center gap-x-6 gap-y-3 ${className}`}>
      <a
        href={site.projects}
        className="press inline-flex min-h-11 items-center gap-2 border border-white/30 bg-white/5 px-6 py-3 text-sm tracking-wider backdrop-blur-sm hover:bg-white/10"
      >
        <ArrowUpRight size={14} aria-hidden="true" />
        ESPLORA I PROGETTI
      </a>
      <a
        href={site.cv}
        className="press inline-flex min-h-11 items-center gap-2 text-sm tracking-wider underline decoration-white/40 underline-offset-[6px] hover:decoration-white"
      >
        VEDI IL CV
      </a>
    </div>
  )
}

export default function App() {
  const menu = useMenu({ closeAbove: '(min-width: 768px)' })
  const driftRef = usePointerDrift<HTMLDivElement>(14)

  useEffect(() => {
    document.documentElement.classList.toggle('menu-open', menu.open)
  }, [menu.open])

  return (
    <div className="relative min-h-[100svh] w-full bg-black text-white">
      <div
        inert={menu.open}
        className="relative z-10 flex min-h-[100svh] flex-col px-5 sm:px-6 md:px-10 lg:px-14"
      >
        {/* 1 · Navbar */}
        <header className="flex items-center justify-between py-6 short:py-4">
          <a href={site.home} className="press -m-1 p-1 hover:opacity-70" aria-label="Benedetta Petrucci, vai alla home del portfolio">
            <Monogram />
          </a>
          <nav aria-label="Navigazione principale" className="hidden md:block">
            <ul className="flex items-center gap-8 text-sm uppercase tracking-wide">
              {navItems.map((item) => (
                <li key={item.label}>
                  <a href={item.href} className="transition-opacity duration-200 hover:opacity-70">
                    {item.label}
                  </a>
                </li>
              ))}
            </ul>
          </nav>
          <button
            ref={menu.triggerRef}
            type="button"
            className="press -mr-2 p-2 md:hidden"
            aria-label="Apri il menu"
            aria-expanded={menu.open}
            aria-controls="menu-a"
            onClick={menu.toggle}
          >
            <Menu size={24} strokeWidth={1.5} aria-hidden="true" />
          </button>
        </header>

        <main className="contents">
          {/* 2 · Meta grid */}
          <div className="mt-4 grid grid-cols-2 gap-4 sm:gap-6 lg:grid-cols-4 lg:gap-8 short:mt-0">
            <div>
              <h1 className="leading-tight">
                <span className="block text-lg tracking-wide md:text-xl">BENEDETTA</span>
                <span className="block font-pixel text-2xl leading-none md:text-3xl">PETRUCCI</span>
              </h1>
              <p className="mt-3 text-[10px] text-white/50" aria-hidden="true">
                *
              </p>
              <p className="mt-1 max-w-[16rem] font-pixel text-lg leading-tight text-white/70">
                Progetto interfacce, identità visive e contenuti. Roma, Italia.
              </p>
            </div>

            <p className="text-right leading-tight lg:text-left">
              <span className="block text-lg tracking-wide md:text-xl">UX/UI &amp;</span>
              <span className="block font-pixel text-2xl leading-none md:text-3xl">VISUAL DESIGN</span>
            </p>

            <section aria-labelledby="a-cosa">
              <h2 id="a-cosa" className="mb-3 font-pixel text-base uppercase tracking-widest text-white/60">
                Cosa faccio
              </h2>
              <p className="max-w-[220px] text-sm leading-relaxed text-white/90">
                Interfacce e sistemi visivi che partono da ricerca e test. Dal 2020 curo comunicazione, eventi e video per FederLUS.
              </p>
            </section>

            <section aria-labelledby="a-competenze" className="text-right lg:text-left">
              <h2 id="a-competenze" className="mb-3 font-pixel text-base uppercase tracking-widest text-white/60">
                Competenze
              </h2>
              <ul className="space-y-0.5 text-sm leading-relaxed text-white/90 max-[359px]:text-[13px]">
                {skills.map((s) => (
                  <li key={s}>{s}</li>
                ))}
              </ul>
            </section>
          </div>

          <Actions className="mt-6 flex desk:hidden" />

          {/* Portrait: in the flow on small or low windows, full-bleed behind the grid on desktop */}
          <figure className="pointer-events-none relative -mx-5 mt-6 h-[min(70svh,600px)] min-h-[340px] sm:min-h-[440px] overflow-hidden sm:-mx-6 md:-mx-10 lg:-mx-14 desk:absolute desk:inset-0 desk:-z-10 desk:m-0 desk:h-auto desk:min-h-0">
            <div aria-hidden="true" className="absolute inset-0 bg-[radial-gradient(ellipse_42%_58%_at_50%_42%,rgba(255,255,255,0.11),transparent_72%)]" />
            <div ref={driftRef} className="absolute inset-0 will-change-transform">
              <PortraitMedia className="absolute left-1/2 top-0 h-full w-auto max-w-none -translate-x-1/2 select-none object-contain [filter:saturate(0.82)_contrast(1.06)] desk:top-[15svh] desk:h-[118svh]" />
            </div>
            {/* Functional scrims: keep headline, CTA and footer legible over the torso */}
            <div aria-hidden="true" className="absolute inset-x-0 bottom-0 h-1/3 bg-gradient-to-t from-black via-black/70 to-transparent desk:h-[46%]" />
            <div aria-hidden="true" className="absolute inset-y-0 left-0 hidden w-1/3 bg-gradient-to-r from-black/70 to-transparent desk:block" />
          </figure>

          {/* 3 · Spacer */}
          <div className="hidden flex-1 desk:block" />

          {/* 4 · Bottom */}
          <div className="relative -mt-28 pb-4 sm:-mt-32 desk:mt-0">
            <div className="grid grid-cols-1 items-end gap-4 sm:gap-6 lg:grid-cols-2">
              <h2 className="text-3xl font-normal uppercase leading-[0.92] tracking-wide sm:text-4xl md:text-5xl lg:text-[3.75rem] xl:text-[4.25rem] short:text-[clamp(2.5rem,8svh,3.75rem)]">
                <span className="block">Do forma</span>
                <span className="block font-pixel text-[1.25em] leading-[0.82]">alle idee,</span>
                <span className="block">progetto</span>
                <span className="block font-pixel text-[1.25em] leading-[0.82]">esperienze</span>
              </h2>

              <div className="flex flex-col justify-end gap-4 sm:gap-6 lg:items-end">
                <Actions className="hidden desk:flex" />
                <ul className="flex flex-wrap gap-2" aria-label="Ambiti">
                  {chips.map((c) => (
                    <li key={c} className="flex items-center gap-2 bg-[#0B0B0B] px-3 py-2 font-pixel text-base uppercase leading-none tracking-wider text-white/85 sm:px-4">
                      <span className="h-1.5 w-1.5 bg-white/60" aria-hidden="true" />
                      {c}
                    </li>
                  ))}
                </ul>
              </div>
            </div>

            <footer className="mt-4 grid grid-cols-1 gap-2 pt-4 text-xs text-white/60 sm:mt-5 sm:grid-cols-2 sm:gap-4 short:mt-3 short:pt-2">
              <p>Roma, Italia · UX/UI design, visual design, comunicazione</p>
              <p className="sm:text-right">
                <a href={site.contacts} className="text-red-500 transition-colors hover:text-red-400">
                  Contattami
                </a>
                <span aria-hidden="true"> · </span>
                <a href={site.linkedin} target="_blank" rel="noopener noreferrer" className="transition-colors hover:text-white">
                  LinkedIn<span className="sr-only"> (si apre in una nuova scheda)</span>
                </a>
              </p>
            </footer>
          </div>
        </main>
      </div>

      {/* 5 · Mobile menu */}
      <div
        id="menu-a"
        ref={menu.panelRef}
        role="dialog"
        aria-modal="true"
        aria-label="Menu"
        data-open={menu.open}
        className="menu-a fixed inset-0 z-50 flex flex-col bg-black/95 backdrop-blur-md md:hidden"
      >
        <div className="flex items-center justify-between px-6 py-6">
          <a href={site.home} onClick={menu.close} aria-label="Benedetta Petrucci, vai alla home del portfolio">
            <Monogram />
          </a>
          <button type="button" className="press -mr-2 p-2" aria-label="Chiudi il menu" onClick={menu.close}>
            <X size={24} strokeWidth={1.5} aria-hidden="true" />
          </button>
        </div>
        <nav aria-label="Navigazione mobile" className="flex flex-1 items-center justify-center pb-24">
          <ul className="flex flex-col items-center gap-8 text-2xl uppercase tracking-widest">
            {navItems.map((item, i) => (
              <li key={item.label} className="menu-a__item" style={{ ['--i' as string]: i }}>
                <a href={item.href} onClick={menu.close} className="press inline-block px-2 py-1">
                  {item.label}
                </a>
              </li>
            ))}
          </ul>
        </nav>
      </div>
    </div>
  )
}
