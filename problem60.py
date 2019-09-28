from itertools import count, islice, combinations, chain
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

  # concat_prime = []
  # combination = combinations(primes, 5)
  # all_primes = []
  # for i, c in enumerate(combination):
  #   for com in combinations(c,2):
  #     concat = int(str(com[0]) + str(com[1]))
  #     isPrime1 = prime(concat)
  #     concat_prime.append(isPrime1)
      
  #   if not False in concat_prime:
  #     all_primes.append(c)
  # return all_primes  

if __name__ == "__main__":
  primes = main()
  rq_prime = final_primes(primes)
  print(rq_prime)