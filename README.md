Axiom
=====

[![Build Status](https://secure.travis-ci.org/tantalor/axiom.png)](http://travis-ci.org/tantalor/axiom)

Axiomatic constructions in python

Synopsis
--------

We are given four "axiom" functions,

 1. `zero()` returns a zero object
 2. `is_zero(obj)` returns `True` if the given object is a zero
 3. `next(obj)` returns the next object from the given object
 4. `prev(obj)` returns the previous object from the given object

This is similiar to how a stack works,

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
