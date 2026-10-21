// Every destination below exists in the portfolio repository.
const root = __SITE_ROOT__

export const site = {
  home: `${root}index.html`,
  projects: `${root}progetti.html`,
  profile: `${root}index.html#profilo`,
  cv: `${root}cv.html`,
  contacts: `${root}contatti.html`,
  linkedin: 'https://www.linkedin.com/in/benedetta-petrucci-5b333b328/',
  portrait: __PORTRAIT__,
} as const

export const portraitAlt = 'Ritratto di Benedetta Petrucci, UX/UI designer'

export type NavItem = { label: string; href: string }

export const navItems: NavItem[] = [
  { label: 'Progetti', href: site.projects },
  { label: 'Profilo', href: site.profile },
  { label: 'CV', href: site.cv },
  { label: 'Contatti', href: site.contacts },
]
