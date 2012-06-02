import unittest

from axiom import *

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

class TestAt(unittest.TestCase):
  def testWithFib(self):
    self.assertTrue(eq(at(fib(), zero()), zero()), "fib[0] = 0")
    self.assertTrue(eq(at(fib(), next(zero())), next(zero())), "fib[1] = 1")
    three = next(next(next(zero())))
    twelve = mult(three, next(three))
    self.assertTrue(eq(at(fib(), twelve), mult(twelve, twelve)), "fib[12] = 144")

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

class TestMultiples(unittest.TestCase):
  def testMultiplesOfZero(self):
    ms = multiples(zero())
    self.assertTrue(eq(ms.next(), zero()), "0 * 1 = 0")
    self.assertTrue(eq(ms.next(), zero()), "0 * 2 = 0")
    self.assertTrue(eq(ms.next(), zero()), "0 * 3 = 0")
  def testMultiplesOfOne(self):
    ms = multiples(next(zero()))
    self.assertTrue(eq(ms.next(), next(zero())), "1 * 1 = 1")
    self.assertTrue(eq(ms.next(), next(next(zero()))), "1 * 2 = 2")
    self.assertTrue(eq(ms.next(), next(next(next(zero())))), "1 * 3 = 3")
  def testMultiples(self):
    three = next(next(next(zero())))
    ms = multiples(three)
    self.assertTrue(eq(ms.next(), three), "1 * 3 = 3")
    self.assertTrue(eq(ms.next(), add(three, three)), "2 * 3 = 6")
    self.assertTrue(eq(ms.next(), add(add(three, three), three)), "3 * 3 = 9")

class TestPowers(unittest.TestCase):
  def testPowersOfZero(self):
    ps = powers(zero())
    self.assertTrue(eq(ps.next(), zero()), "0^1 = 0")
    self.assertTrue(eq(ps.next(), zero()), "0^2 = 0")
    self.assertTrue(eq(ps.next(), zero()), "0^3 = 0")
  def testPowersOfOne(self):
    ps = powers(next(zero()))
    self.assertTrue(eq(ps.next(), next(zero())), "1^1 = 1")
    self.assertTrue(eq(ps.next(), next(zero())), "1^2 = 1")
    self.assertTrue(eq(ps.next(), next(zero())), "1^3 = 1")
  def testPowers(self):
    three = next(next(next(zero())))
    ps = powers(three)
    self.assertTrue(eq(ps.next(), three), "3^1 = 1")
    self.assertTrue(eq(ps.next(), mult(three, three)), "3^2 = 9")
    self.assertTrue(eq(ps.next(), mult(mult(three, three), three)), "3^3 = 27")

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

class TestFib(unittest.TestCase):
  def testFib(self):
    fibs = fib()
    a = next(zero())
    b = add(a,a)
    c = add(a,b)
    d = add(b,c)
    e = add(c,d)
    f = add(d,e)
    self.assertTrue(eq(fibs.next(), zero()), 'fib[0] = 0')
    self.assertTrue(eq(fibs.next(), a), 'fib[1] = 1')
    self.assertTrue(eq(fibs.next(), a), 'fib[1] = 1')
    self.assertTrue(eq(fibs.next(), b), 'fib[1] = 2')
    self.assertTrue(eq(fibs.next(), c), 'fib[1] = 3')
    self.assertTrue(eq(fibs.next(), d), 'fib[1] = 5')
    self.assertTrue(eq(fibs.next(), e), 'fib[1] = 8')
    self.assertTrue(eq(fibs.next(), f), 'fib[1] = 13')

class TestFact(unittest.TestCase):
  def testFact(self):
    facts = fact()
    a = next(zero())
    b = next(a)
    c = next(b)
    d = next(c)
    e = next(d)
    self.assertTrue(eq(facts.next(), a), "0! = 1")
    self.assertTrue(eq(facts.next(), a), "1! = 1")
    self.assertTrue(eq(facts.next(), b), "2! = 2")
    self.assertTrue(eq(facts.next(), mult(b,c)), "3! = 6")
    self.assertTrue(eq(facts.next(), mult(mult(b,c),d)), "4! = 24")
    self.assertTrue(eq(facts.next(), mult(mult(mult(b,c),d),e)), "4! = 120")

class TestPrimes(unittest.TestCase):
  def testPrimes(self):
    ps = primes()
    two = ps.next()
    three = ps.next()
    five = ps.next()
    seven = ps.next()
    eleven = ps.next()
    thirteen = ps.next()
    seventeen = ps.next()
    self.assertTrue(eq(two, next(next(zero()))), "p[0] = 2")
    self.assertTrue(eq(three, next(two)), "p[1] = p[0]+1 = 3")
    self.assertTrue(eq(five, add(two, three)), "p[2]=p[0]+p[1]=5")
    self.assertTrue(eq(seven, add(two, five)), "p[3]=p[0]+p[2]=7")
    self.assertTrue(eq(eleven, prev(add(five, seven))), "p[4]=p[2]+p[3]-1=11")
    self.assertTrue(eq(thirteen, next(add(five, seven))), "p[5]=p[2]+p[3]+1=13")
    self.assertTrue(eq(seventeen, prev(add(seven, eleven))), "p[6]=p[3]+p[5]-1=17")

class TestPascalColumn(unittest.TestCase):
  def testZero(self):
    ps = pascal_column(zero())
    one = next(zero())
    self.assertTrue(eq(ps.next(), one), "0 choose 0 = 1")
    self.assertTrue(eq(ps.next(), one), "1 choose 0 = 1")
    self.assertTrue(eq(ps.next(), one), "2 choose 0 = 1")
    self.assertTrue(eq(ps.next(), one), "3 choose 0 = 1")
  def testOne(self):
    one = next(zero())
    two = next(one)
    three = next(two)
    four = next(three)
    ps = pascal_column(prev(two))
    self.assertTrue(eq(ps.next(), one),   "1 choose 1 = 1")
    self.assertTrue(eq(ps.next(), two),   "2 choose 1 = 2")
    self.assertTrue(eq(ps.next(), three), "3 choose 1 = 3")
    self.assertTrue(eq(ps.next(), four),  "4 choose 1 = 4")
  def testTwo(self):
    one = next(zero())
    three = next(next(one))
    six = add(three, three)
    ten = next(mult(three, three))
    ps = pascal_column(prev(three))
    self.assertTrue(eq(ps.next(), one),   "2 choose 2 = 1")
    self.assertTrue(eq(ps.next(), three), "3 choose 2 = 3")
    self.assertTrue(eq(ps.next(), six),   "4 choose 2 = 6")
    self.assertTrue(eq(ps.next(), ten),   "5 choose 2 = 10")
  def testThree(self):
    one = next(zero())
    four = next(next(next(one)))
    ten = next(next(add(four,four)))
    twenty = add(ten,ten)
    ps = pascal_column(prev(four))
    self.assertTrue(eq(ps.next(), one),    "3 choose 3 = 1")
    self.assertTrue(eq(ps.next(), four),   "4 choose 3 = 4")
    self.assertTrue(eq(ps.next(), ten),    "5 choose 3 = 10")
    self.assertTrue(eq(ps.next(), twenty), "6 choose 3 = 20")
  def testFour(self):
    one = next(zero())
    five = next(next(next(next(one))))
    fifteen = add(add(five,five),five)
    thirtyfive = add(add(fifteen, fifteen), five)
    ps = pascal_column(prev(five))
    self.assertTrue(eq(ps.next(), one),        "4 choose 4 = 1")
    self.assertTrue(eq(ps.next(), five),       "5 choose 4 = 5")
    self.assertTrue(eq(ps.next(), fifteen),    "6 choose 4 = 15")
    self.assertTrue(eq(ps.next(), thirtyfive), "7 choose 4 = 35")

class TestPascalRow(unittest.TestCase):
  def testZero(self):
    ps = list(pascal_row(zero()))
    one = next(zero())
    self.assertEquals(len(ps), 1)
    self.assertTrue(eq(ps[0], one), "0 choose 0 = 1")
  def testOne(self):
    one = next(zero())
    ps =  list(pascal_row(one))
    self.assertEquals(len(ps), 2)
    self.assertTrue(eq(ps[0], one), "1 choose 0 = 1")
    self.assertTrue(eq(ps[1], one), "1 choose 1 = 1")
  def testTwo(self):
    one = next(zero())
    two = next(one)
    ps =  list(pascal_row(two))
    self.assertEquals(len(ps), 3)
    self.assertTrue(eq(ps[0], one), "2 choose 0 = 1")
    self.assertTrue(eq(ps[1], two), "2 choose 1 = 2")
    self.assertTrue(eq(ps[2], one), "2 choose 2 = 1")
  def testThree(self):
    one = next(zero())
    three = next(next(one))
    ps =  list(pascal_row(three))
    self.assertEquals(len(ps), 4)
    self.assertTrue(eq(ps[0], one),   "3 choose 0 = 1")
    self.assertTrue(eq(ps[1], three), "3 choose 1 = 3")
    self.assertTrue(eq(ps[2], three), "3 choose 2 = 3")
    self.assertTrue(eq(ps[3], one),   "3 choose 3 = 1")
  def testFour(self):
    one = next(zero())
    four = next(next(next(one)))
    six = next(next(four))
    ps = list(pascal_row(four))
    self.assertEquals(len(ps), 5)
    self.assertTrue(eq(ps[0], one),  "4 choose 0 = 1")
    self.assertTrue(eq(ps[1], four), "4 choose 1 = 4")
    self.assertTrue(eq(ps[2], six),  "4 choose 2 = 6")
    self.assertTrue(eq(ps[3], four), "4 choose 3 = 4")
    self.assertTrue(eq(ps[4], one),  "4 choose 4 = 1")

class TestChoose(unittest.TestCase):
  def testChoose(self):
    one = next(zero())
    two = next(one)
    three = next(two)
    self.assertTrue(eq(choose(zero(), zero()), one), "0 choose 0 = 1")
    self.assertRaises(Exception, lambda: choose(zero(), one), "0 choose 1")
    self.assertTrue(eq(choose(one, zero()), one), "1 choose 0 = 1")
    self.assertTrue(eq(choose(one, one), one),    "1 choose 1 = 1")
    self.assertRaises(Exception, lambda: choose(one, two), "1 choose 2")
    self.assertTrue(eq(choose(two, zero()), one), "2 choose 0 = 1")
    self.assertTrue(eq(choose(two, one), two),    "2 choose 1 = 2")
    self.assertTrue(eq(choose(two, two), one),    "2 choose 2 = 1")
    self.assertRaises(Exception, lambda: choose(two, three), "2 choose 3")
    self.assertTrue(eq(choose(three, zero()), one), "3 choose 0 = 1")
    self.assertTrue(eq(choose(three, one), three),  "3 choose 1 = 3")
    self.assertTrue(eq(choose(three, two), three),  "3 choose 2 = 3")
    self.assertTrue(eq(choose(three, three), one),  "3 choose 3 = 1")

unittest.main()
