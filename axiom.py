## 0 (universe)

def compose(step, arg):
  """Yields the step composed with itself on the argument."""
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
  """Yields next objects from zero."""
  return compose(next, zero())

def up_to(to):
  """Yield objects from zeros up to the given object, exclusive."""
  val = zero()
  while not is_zero(to):
    yield val
    val = next(val)
    to = prev(to)

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

def eq(left, right):
  """True if left and right are the same values"""
  return is_zero(dist(left, right))

def mult(left, right):
  """Left times right."""
  if is_zero(left): return zero()
  step = lambda (right, result): (prev(right), add(result, left))
  for (right, result) in compose(step, (right, zero())):
    if is_zero(right):
      return result

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

def exp(b, p):
  """Left times left times left, etc. right times."""
  if is_zero(p) and is_zero(b):
    raise Exception("Cannot raise zero to zero")
  out = next(zero())
  for _ in up_to(p):
    out = mult(out, b)
  return out

def fib():
  """Fibonacci numbers beginning with zero."""
  step = lambda (a, b): (b, add(a,b))
  yield zero()
  for (a, b) in compose(step, (zero(), next(zero()))):
    yield b

if __name__ == '__main__':
  unittest.main()

