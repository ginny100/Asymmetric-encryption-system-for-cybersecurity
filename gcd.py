def gcd(a = 1, b = 1):
  if b == 0:
    return a
  else:
    print(a % b)
    return gcd(b, a % b)
    
