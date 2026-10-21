import type { Config } from 'tailwindcss'

export default {
  content: ['./app/**/*.html', './src/**/*.{ts,tsx}'],
  theme: {
    extend: {
      screens: {
        // Single-viewport composition only where the window is wide AND tall enough.
        desk: { raw: '(min-width: 1024px) and (min-height: 600px)' },
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
