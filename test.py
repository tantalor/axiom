import unittest

from axiom import\
  zero, is_zero, prev, next,\
  counting, up_to, add, dist,\
  gt, eq, mult, div, exp

class TestIsZero(unittest.TestCase):
  def testIsZero(self):
    self.assertTrue(is_zero(zero()), "0 = 0")

class TestPrev(unittest.TestCase):
  def testPrev(self):
    self.assertTrue(is_zero(prev(next(zero()))), "1-1 = 0")
    self.assertRaises(Exception, lambda: prev(zero()))

class TestCounting(unittest.TestCase):
  def testCounting(self):
    g = counting()
    self.assertTrue(is_zero(g.next()), "0")
    self.assertTrue(is_zero(prev(g.next())), "1")
    self.assertTrue(is_zero(prev(prev(g.next()))), "2")

class TestUpTo(unittest.TestCase):
  def testEmpty(self):
    r = up_to(zero())
    self.assertRaises(Exception, r.next)
  def testUpTo(self):
    r = up_to(next(next(next(zero()))))
    self.assertTrue(is_zero(r.next()), "0")
    self.assertTrue(is_zero(prev(r.next())), "1")
    self.assertTrue(is_zero(prev(prev(r.next()))), "2")
    self.assertRaises(Exception, r.next)

class TestAdd(unittest.TestCase):
  def testAdd(self):
    self.assertTrue(is_zero(add(zero(), zero())), "0+0 = 0")
    self.assertTrue(is_zero(prev(add(next(zero()), zero()))), "(0+1)-1 = 0")
    self.assertTrue(is_zero(prev(add(zero(), next(zero())))), "(1+0)-1 = 0")
    self.assertTrue(is_zero(prev(prev(add(next(zero()), next(zero()))))), "(1+1)-1-1 = 0")

class TestDist(unittest.TestCase):
  def testDist(self):
    self.assertTrue(is_zero(dist(zero(), zero())), "(0-0) = 0")
    self.assertTrue(is_zero(prev(dist(zero(), next(zero())))), "(1-0)-1 = 0")
    self.assertTrue(is_zero(dist(next(zero()), next(zero()))), "(1-1) = 0")

class TestGt(unittest.TestCase):
  def testGt(self):
    self.assertFalse(gt(zero(), zero()), "0 <= 0")
    self.assertTrue(gt(next(zero()), zero()), "1 > 0")
    self.assertFalse(gt(zero(), next(zero())), "0 <= 1")
    self.assertFalse(gt(next(zero()), next(zero())), "1 <= 1")

class TestEq(unittest.TestCase):
  def testEq(self):
    self.assertTrue(eq(zero(), zero()), "0 = 0")
    self.assertFalse(eq(next(zero()), zero()), "0+1 != 0")
    self.assertFalse(eq(zero(), next(zero())), "0 != 0+1")
    self.assertTrue(eq(next(zero()), next(zero())), "0+1 = 0+1" )

class TestMult(unittest.TestCase):
  def testMult(self):
    self.assertTrue(is_zero(mult(zero(), zero())), "0 * 0 = 0")
    self.assertTrue(is_zero(mult(next(zero()), zero())), "0 * 1 = 0")
    self.assertTrue(is_zero(mult(zero(), next(zero()))), "1 * 0 = 0")
    self.assertTrue(eq(mult(next(zero()), next(zero())), next(zero())), "1 * 1 = 1")
    self.assertTrue(eq(mult(next(next(zero())), next(next(zero()))), next(next(next(next(zero()))))), "2 * 2 = 4")

class TestDiv(unittest.TestCase):
  def testDiv(self):
    self.assertRaises(Exception, lambda: div(zero(), zero()), "0/0")
    self.assertRaises(Exception, lambda: div(next(zero()), zero()), "1/0")
    (q, r) = div(zero(), next(zero()))
    self.assertTrue(eq(q, zero()), "0/1 = 0")
    self.assertTrue(eq(r, zero()), "0 % 1 = 0")
    (q, r) = div(next(zero()), next(zero()))
    self.assertTrue(eq(q, next(zero())), "1/1 == 1")
    self.assertTrue(is_zero(r), "1 % 0 == 0")
    (q, r) = div(next(next(next(zero()))), next(next(zero())))
    self.assertTrue(eq(q, next(zero())), "3/2 == 1")
    self.assertTrue(eq(r, next(zero())), "3 % 2 == 1")
    (q, r) = div(next(next(zero())), next(next(next(zero()))))
    self.assertTrue(eq(q, zero()), "2/3 == 0")
    self.assertTrue(eq(r, next(next(zero()))), "2 % 3 == 2")

class TestExp(unittest.TestCase):
  def testExp(self):
    self.assertRaises(Exception, lambda: exp(zero(), zero()), "0^0")
    self.assertTrue(is_zero(prev(exp(next(next(zero())), zero()))), "2^0 = 1")
    self.assertTrue(is_zero(exp(zero(), next(next(zero())))), "0^2 = 0")    
    self.assertTrue(is_zero(
      prev(prev(prev(prev(
        exp(next(next(zero())), next(next(zero())))
      ))))
    ), "2^2 = 4")

unittest.main()
