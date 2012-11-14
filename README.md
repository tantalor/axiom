Axiom
=====

[![Build Status](https://secure.travis-ci.org/tantalor/axiom.png)](http://travis-ci.org/tantalor/axiom)

An axiomatic number system in python

Synopsis
--------

We are given four "axiom" functions,

 1. `zero()` returns a zero object
 2. `is_zero(obj)` returns `True` if the given object is a zero
 3. `next(obj)` returns the next object from the given object
 4. `prev(obj)` returns the previous object from the given object

This is similar to how a stack works,

    >>> from axiom import zero, is_zero, next, prev
    >>> is_zero(zero())
    True
    >>> is_zero(next(zero()))
    False
    >>> is_zero(prev(next(zero())))
    True

Nothing is less than than a zero object.

Objects are not necessarily immutable (e.g., a `list`). This constraint might be added later.

Arbitrary loops (e.g., `while`, recursion) are forbidden. Iterate over generators instead.

We have one general-purpose generator,

 * `compose(fn, arg)` yields `arg`, `fn(arg)`, `fn(fn(arg))`, etc.
 
Derived functions are grouped by depth from the axioms. For example, we group `dist` and `add` because they are derived from the axioms. We group `eq` and `multiples` because they are derived from `dist` and `add` (respectively).

There are exceptions, such as dividing by zero.

By convention, 0<sup>0</sup> equals 1 and does not throw an exception.

Sequences
---------

Some useful sequences may be generated,

 * `counting()` yields 0 1 2 3 4...
 * `fib()` yields 0 1 1 2 3 5 8 13...
 * `multiples(n)` yields n 2n 3n 4n 5n...
 * `primes()` yields 2 3 5 7 11 13 17 19...
 * `catalan()` yields 1 1 2 5 14 42 132...
 * `fact()` yields 1 1 2 6 24 120...
 * `powers(n)` yields 1 n n<sup>2</sup> n<sup>3</sup> n<sup>4</sup> n<sup>5</sup>...
 * `pascal_column(k)` yields kth column of Pascal's triangle
 * `pascal_row(n)` yields nth row of Pascal's triangle
