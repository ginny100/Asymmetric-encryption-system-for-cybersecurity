def extended_gcd(a = 1, b = 1):
  if a < b:
    a, b = b, a
    print('Switched two arguments to ensure a >= b.')
  if b == 0:
    return(l, 0, a)
  (x, y, d) = extended_gcd(b, a % b)
  return y, x - a//b * y, d
