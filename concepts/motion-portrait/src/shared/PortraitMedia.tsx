import { portraitAlt, site } from './site'

type Props = {
  className?: string
  /**
   * Reserved for a future personal clip (not produced yet). When set, a muted looping
   * video replaces the still, with the still as poster; reduced motion keeps the still.
   */
  videoSrc?: string
  priority?: boolean
}

export function PortraitMedia({ className = '', videoSrc, priority = true }: Props) {
  const reduce = typeof window !== 'undefined' && window.matchMedia('(prefers-reduced-motion: reduce)').matches

  if (videoSrc && !reduce) {
    return (
      <video className={className} src={videoSrc} poster={site.portrait} autoPlay muted loop playsInline aria-label={portraitAlt} />
    )
  }

  return (
    <img
      className={className}
      src={site.portrait}
      width={1086}
      height={1448}
      alt={portraitAlt}
      decoding="async"
      fetchPriority={priority ? 'high' : 'auto'}
    />
  )
}
