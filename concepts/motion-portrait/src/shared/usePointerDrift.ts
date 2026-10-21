import { useEffect, useRef } from 'react'

/**
 * Slow drift of the portrait toward the pointer. Decorative only: runs on fine pointers
 * with hover, never with reduced motion, and writes transform directly (no re-render).
 */
export function usePointerDrift<T extends HTMLElement>(strength = 10) {
  const ref = useRef<T>(null)

  useEffect(() => {
    const el = ref.current
    if (!el) return
    const fine = window.matchMedia('(hover: hover) and (pointer: fine)')
    const reduce = window.matchMedia('(prefers-reduced-motion: reduce)')
    if (!fine.matches || reduce.matches) return

    let tx = 0, ty = 0, x = 0, y = 0, frame = 0
    const onMove = (e: PointerEvent) => {
      tx = (e.clientX / window.innerWidth - 0.5) * -strength
      ty = (e.clientY / window.innerHeight - 0.5) * -strength * 0.5
      if (!frame) frame = requestAnimationFrame(tick)
    }
    const tick = () => {
      x += (tx - x) * 0.06
      y += (ty - y) * 0.06
      el.style.transform = `translate3d(${x.toFixed(2)}px, ${y.toFixed(2)}px, 0)`
      frame = Math.abs(tx - x) + Math.abs(ty - y) > 0.05 ? requestAnimationFrame(tick) : 0
    }
    window.addEventListener('pointermove', onMove, { passive: true })
    return () => {
      window.removeEventListener('pointermove', onMove)
      cancelAnimationFrame(frame)
      el.style.transform = ''
    }
  }, [strength])

  return ref
}
