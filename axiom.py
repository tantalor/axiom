## 0 (universe)

def compose(step, arg):
  """Yields arg, step(arg), step(step(arg)), etc."""
  while True:
    yield arg
    arg = step(arg)

## 1 (axioms)

def zero():
  """A zero."""
  return ()

def is_zero(arg):
  """True if the argument is zero."""
  return arg is zero()

def next(arg):
  """Next object from argument."""
  return (arg,)

def prev(arg):
  """Inverse of next."""
  if is_zero(arg):
    raise Exception("Nothing is before zero.")
  return arg[0]

## 2

def counting():
  """Yields zero(), next(zero()), next(next(zero())), etc."""
  return compose(next, zero())

def at(g, to):
  """to-th object in the given generator, from zero."""
  for t in compose(prev, to):
    if is_zero(t): return g.next()
    g.next()

def minus(left, right):
  """Returns (left>right, |left-right|)"""
  step = lambda (l, r): (prev(l), prev(r))
  for (left, right) in compose(step, (left, right)):
    if is_zero(left): return (False, right)
    if is_zero(right): return (True, left)

## 3

def dist(left, right):
  """Returns |left-right|"""
  return minus(left, right)[1]

def gt(left, right):
  """Returns left > right"""
  return minus(left, right)[0]

def add(left, right):
  return at(compose(next, left), right)

def up_to(to, g=None):
  """Yields to objects from the given generator."""
  if not g: g = counting()
  for t in compose(prev, to):
    if is_zero(t): return
    yield g.next()

## 4

def eq(left, right):
  """True if left and right are the same values"""
  return is_zero(dist(left, right))

def fib():
  """Yields fibonacci numbers: 0, 1, 1, 2, 3, 5, 8, 13, etc."""
  step = lambda (a, b): (b, add(a,b))
  yield zero()
  for (a, b) in compose(step, (zero(), next(zero()))):
    yield b

def multiples(n):
  """Yields n, 2n, 3n, 4n, etc."""
  return compose(lambda m: add(m,n), n)

def div(n, d):
  """Returns (q, r) such that q * n + r = d and r < n"""
  if is_zero(d):
    raise Exception("Cannot divide by zero")
  for q in counting():
    for r in up_to(d):
      if is_zero(n):
        return (q, r)
      else:
        n = prev(n)

## 5

def mult(left, right):
  """Left times right."""
  if is_zero(right): return zero()
  return at(multiples(left), prev(right))

def primes():
  """Yields prime numbers."""
  known = list() # (generator, last), ...
  two = next(next(zero()))
  three = next(two)
  yield two
  yield three
  # test every 6n-1 and 6n+1
  for six in multiples(add(three, three)): # 6, 12, 18, etc...
    for candidate in (prev(six), next(six)):
      is_prime = True
      # TO DO: use a heap instead
      for (i, (generator, last)) in enumerate(known):
        if eq(candidate, last):
          known[i] = (generator, generator.next())
          is_prime = False
      if is_prime:
        yield candidate
        generator = multiples(candidate)
        generator.next() # skip to 2n
        known.append((generator, generator.next()))

## 6

def fact():
  """Yields factorial numbers: 1, 1, 2, 6, 24, 120, etc."""
  step = lambda (n, f): (next(n), mult(n, f))
  for (n, f) in compose(step, (next(zero()), next(zero()))):
    yield f

def powers(n):
  """Yields n, n^2, n^3, etc."""
  return compose(lambda p: mult(p,n), n)

def pascal_column(k):
  """Yields k-th column of pascal's triangle."""
  p = next(zero())
  for n in compose(next, next(k)):
    yield p
    (p, _) = div(mult(p, n), dist(n, k))

## 7

def exp(b, p):
  """Left times left times left, etc. right times."""
  if is_zero(p) and is_zero(b):
    raise Exception("Cannot raise zero to zero")
  if is_zero(p):
    return next(zero())
  return at(powers(b), prev(p))

def choose(n, k):
  """Returns n choose k."""
  (positive, diff) = minus(n, k)
  if not positive and not eq(diff, zero()):
    raise Exception("Out of bounds")
  return at(pascal_column(k), diff)
