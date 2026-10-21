import { useCallback, useEffect, useRef, useState } from 'react'

const FOCUSABLE = 'a[href], button:not([disabled]), [tabindex]:not([tabindex="-1"])'

/**
 * Disclosure/dialog state for the navigation menus: Escape closes, focus moves into
 * the panel, Tab is trapped inside it and focus returns to the trigger on close.
 * `closeAbove` closes the menu when the viewport grows past the breakpoint that hides it;
 * `trapTrigger` keeps the trigger in the Tab cycle when it stays visible beside the panel.
 */
export function useMenu({ closeAbove, trapTrigger = false }: { closeAbove?: string; trapTrigger?: boolean } = {}) {
  const [open, setOpen] = useState(false)
  const triggerRef = useRef<HTMLButtonElement>(null)
  const panelRef = useRef<HTMLDivElement>(null)
  const wasOpen = useRef(false)

  const close = useCallback(() => setOpen(false), [])
  const toggle = useCallback(() => setOpen((v) => !v), [])

  useEffect(() => {
    if (open) {
      wasOpen.current = true
      const first = panelRef.current?.querySelector<HTMLElement>(FOCUSABLE)
      first?.focus()
    } else if (wasOpen.current) {
      wasOpen.current = false
      triggerRef.current?.focus()
    }
  }, [open])

  useEffect(() => {
    if (!open) return
    const onKey = (e: KeyboardEvent) => {
      if (e.key === 'Escape') {
        e.preventDefault()
        setOpen(false)
        return
      }
      if (e.key !== 'Tab' || !panelRef.current) return
      const items = [trapTrigger ? triggerRef.current : null, ...panelRef.current.querySelectorAll<HTMLElement>(FOCUSABLE)].filter(
        (el): el is HTMLElement => !!el && el.offsetParent !== null,
      )
      if (items.length === 0) return
      const first = items[0]
      const last = items[items.length - 1]
      const active = document.activeElement
      if (e.shiftKey && (active === first || !items.includes(active as HTMLElement))) {
        e.preventDefault()
        last.focus()
      } else if (!e.shiftKey && (active === last || !items.includes(active as HTMLElement))) {
        e.preventDefault()
        first.focus()
      }
    }
    document.addEventListener('keydown', onKey)
    return () => document.removeEventListener('keydown', onKey)
  }, [open, trapTrigger])

  useEffect(() => {
    if (!open || !closeAbove) return
    const mq = window.matchMedia(closeAbove)
    const onChange = () => mq.matches && setOpen(false)
    mq.addEventListener('change', onChange)
    return () => mq.removeEventListener('change', onChange)
  }, [open, closeAbove])

  return { open, toggle, close, triggerRef, panelRef }
}
