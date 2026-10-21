// Original BP monogram drawn on a 5x7 pixel grid per letter.
const B = ['11110', '10001', '10001', '11110', '10001', '10001', '11110']
const P = ['11110', '10001', '10001', '11110', '10000', '10000', '10000']

const cells = [B, P].flatMap((letter, l) =>
  letter.flatMap((row, y) =>
    [...row].flatMap((bit, x) => (bit === '1' ? [{ x: x + l * 6, y: y + 2 }] : [])),
  ),
)

export function Monogram({ className = 'h-7 w-7' }: { className?: string }) {
  return (
    <svg className={className} viewBox="0 0 11 11" fill="currentColor" shapeRendering="crispEdges" aria-hidden="true" focusable="false">
      {cells.map(({ x, y }) => (
        <rect key={`${x}-${y}`} x={x} y={y} width="1" height="1" />
      ))}
    </svg>
  )
}
