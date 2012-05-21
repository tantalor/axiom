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
  while not is_zero(to):
    to = prev(to)
    g.next()
  return g.next()

def add(left, right):
  """Left plus right."""
  step = lambda (left, right): (next(left), prev(right))
  for (left, right) in compose(step, (left, right)):
    if is_zero(right):
      return left

def dist(left, right):
  """Distance between left and right."""
  step = lambda (l, r): (prev(l), prev(r))
  for (left, right) in compose(step, (left, right)):
    if is_zero(left) and is_zero(right):
      return zero()
    # one of them is zero
    if is_zero(left): return right
    if is_zero(right): return left

def gt(left, right):
  """True if left is greater than right."""
  step = lambda (l, r): (prev(l), prev(r))
  for (left, right) in compose(step, (left, right)):
    if is_zero(left): return False
    if is_zero(right): return True

## 3

def up_to(to):
  """Yields to objects from the given generator."""
  g = counting()
  for t in compose(prev, to):
    if is_zero(t): return
    yield g.next()

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

## 4

def div(n, d):
  """Quotient (q) and remainder (r) such that q*n+r = d"""
  if is_zero(d):
      raise Exception("Cannot divide by zero")
  for q in counting():
    for r in up_to(d):
      if is_zero(n):
        return (q, r)
      else:
        n = prev(n)

def mult(left, right):
  """Left times right."""
  if is_zero(right): return zero()
  return at(multiples(left), prev(right))

def fact():
  """Yields factorial numbers: 1, 1, 2, 6, 24, 120, etc."""
  step = lambda (n, f): (next(n), mult(n, f))
  for (n, f) in compose(step, (next(zero()), next(zero()))):
    yield f

## 5

def powers(n):
  """Yields n, n^2, n^3, etc."""
  return compose(lambda p: mult(p,n), n)

## 6

def exp(b, p):
  """Left times left times left, etc. right times."""
  if is_zero(p) and is_zero(b):
    raise Exception("Cannot raise zero to zero")
  if is_zero(p):
      return next(zero())
  return at(powers(b), prev(p))
