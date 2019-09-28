"""
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes 
and concatenating them in any order the result will always be prime. For example, 
taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, 
represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

"""

from itertools import count, islice
from math import sqrt
import random

def prime(n):
  
  if n <2:
    return False
   
  for i in islice(count(2), int(sqrt(n) -1)):
    if n %i==0:
      return False

  return True

def main():
  primes = []
  for p in range(2, 10000):
    isPrime = prime(p)

    if isPrime:
      primes.append(p)
  return primes

def gen_primes(a,b):
    ab = int(str(a) + str(b))
    ba = int(str(b) + str(a))

    isPrime1 = prime(ab)
    isPrime2 = prime(ba)

    if isPrime2 and isPrime1:
      return True
    return False

def final_primes(primes):

  for a in primes:
    for b in primes:

      if b > a:
        if gen_primes(a, b):
          for c in primes:
            if c > b:
              if gen_primes(a, c) and gen_primes(b, c):

                for d in primes:
                  if gen_primes(a, d) and gen_primes(b, d) and gen_primes(c, d):

                    for e in primes:
                      if gen_primes(a, e) and gen_primes(b, e) and gen_primes(c, e) and gen_primes(d, e):
                        return a + b + c + d + e

if __name__ == "__main__":
  primes = main()
  rq_prime = final_primes(primes)
  print(rq_prime)