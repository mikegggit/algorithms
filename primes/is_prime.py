#!/usr/bin/python

import math;

"""Checking primality of a number."""

def isPrimeDum(n):
  """non-optimized method.

  Check every number between 2 and n - 1 and see if we can evenly divide into n.

  Extremely inefficient."""
  
  for i in range(2, n):
    if n % i == 0:
      return False

  return True


def isPrimeSqrt(n):
  """Only check up to the square root of n.
 
  If n weren't prime, then it could be factored into a * b, with either both a and 
  b equal to sqr(n) or one of a or b less than sqr(n).  If we can't find a factor up 
  to and including sqr(n), n must be prime.
  """
  
  i = 2
  while i <= math.sqrt(n):
    if n % i == 0:
      return False
  
    i += 1

  return True 


if __name__ == "__main__":
  print(isPrimeDum(7))
  print(isPrimeDum(20000))
  print(isPrimeDum(199999))

  print(isPrimeSqrt(7))
  print(isPrimeSqrt(20000))
  print(isPrimeSqrt(199999))
