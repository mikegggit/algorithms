#!/usr/bin/python

"""Sieve of Eratosthenes

See https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes.

An algorithm for determining prime numbers up do some max.  

The algorithm works by taking multiples of primes, starting at 2, and 
marking them as non-prime.  The resulting non prime-multiple between 2 and 
some max are prime.


Analysis:
Good for smaller primes.

Suffers from memory requirements for larger primes.

"""


def getPrimes(max):
  
  # potentials
  sieve = [True for n in range(0,max+1)]

  # filter out non-sieve
  for i, v in enumerate(sieve):
  
    # start processing at 2...
    if i < 2:
      continue

    # skip those already marked non-prime
    if not v:
      continue

    # current prime multiplier
    multiplier = 2

    multiple = multiplier * i

    # mark multiples of current prime non-prime...
    while (multiple <= max):
      #print("i={}, multipler={}, multiple={}, sieve[multiple]={}".format(i, multiplier, multiple, sieve[multiple]))
      sieve[multiple] = False
      multiplier += 1
      multiple = i * multiplier
 
  
  # list primes
  primes = [ i for i, v in enumerate(sieve) if v and i > 1 ]
  return primes

if __name__ == "__main__":
  print(getPrimes(200))
