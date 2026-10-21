import type { Config } from 'tailwindcss'

export default {
  content: ['./app/**/*.html', './src/**/*.{ts,tsx}'],
  theme: {
    extend: {
      screens: {
        // Single-viewport composition only where the window is wide AND tall enough.
        desk: { raw: '(min-width: 1024px) and (min-height: 540px)' },
        // Laptops and in-app previews (~590-760px tall): compact spacing so title and CTA fit the first screen.
        short: { raw: '(min-width: 1024px) and (min-height: 540px) and (max-height: 760px)' },
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
        // Provisional stand-in for basis33 (see README): VT323, SIL OFL.
        pixel: ['VT323', 'ui-monospace', 'monospace'],
        // Provisional stand-in for Askan Light (commercial, Hoftype): Newsreader, SIL OFL.
        serif: ['Newsreader', 'Georgia', 'serif'],
      },
    },
  },
  plugins: [],
} satisfies Config
