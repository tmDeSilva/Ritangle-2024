import math
from functools import lru_cache

def convert(*args):
    result = 0
    for i in range(len(args)):
        result += args[i] * 10 ** (len(args) - 1 - i)
    return result

def findZeros(pNumber):
     while pNumber != 0:
          if pNumber % 10 == 0:
               return True
          pNumber = (pNumber - pNumber % 10) // 10

     return False

def getDigits(pNumber):
     result = []

     while pNumber != 0:
          result.append(pNumber % 10)
          pNumber = (pNumber - pNumber % 10) // 10

     return result[::-1]


cubes = [n ** 3 for n in range(math.ceil(100**(1/3)), math.floor(1000**(1/3))+1)]

index = 1
remaining = [int(i) for i in range(1,1000,2)]
while index < len(remaining):
     sieve = set()
     for i in range(remaining[index] - 1, len(remaining),remaining[index]):
          sieve |= {remaining[i]}

     remaining = sorted(set(remaining) - sieve)
     index += 1

luckyNumbers = [n for n in remaining if 100 <= n and n < 1000]

def is_happy(n,s = set()):
     if n == 1:
          return True
     if n in s:
          return False
     return is_happy(sum([(int(i))**2 for i in str(n)]), s | {n})

happyNumbers = [n for n in range(100,1000) if is_happy(n)]

@lru_cache(maxsize=None)
def is_prime(n): 
    if n <= 1: 
        return False 
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False 
    return True 

fourDigitPrimes = []
for i in range(1000,10000):
     if is_prime(i):
          fourDigitPrimes.append(i)

def lucasGenerator(x):
    if x == 0:
        return 2
    if x == 1:
        return 1
    
    return lucasGenerator(x-1) + lucasGenerator(x-2)

lucasNumbers = [lucasGenerator(n) for n in range(20) if 100 <= lucasGenerator(n) and lucasGenerator(n) < 1000]
cullenNumbers = [n * 2 ** n + 1 for n in range(20) if 100 <= n * 2 ** n + 1 and n * 2 ** n + 1 < 1000]

divisorable = []
for pN in range(100,1000):
    T = set()
    for iN in range(1,math.ceil(pN ** (1/2))+1):
            if pN%iN == 0:
                T |= {iN, pN//iN}

    if pN % len(T) == 0:
         divisorable.append(pN)


def fibonacciGenerator(x):
    if x == 0:
        return 2
    if x == 1:
        return 1
    
    return fibonacciGenerator(x-1) + fibonacciGenerator(x-2)

fibonacciNumbers = [fibonacciGenerator(n) for n in range(20) if 100 <= fibonacciGenerator(n) and fibonacciGenerator(n) < 1000]
squares = [n**2 for n in range(10,32)]
triangular = [n * (n+1) // 2 for n in range(int((-1/2 + (2 * 100) + 1/4)**(1/2)),int((-1/2 + (2 * 1000) + 1/4)**(1/2))+1)]

harshad = []
for i in range(1,1000):
     if i % sum([int(j) for j in getDigits(i)]) == 0:
          harshad.append(i)

cubeSumIsSquare = []
for i in range(1000,10000):
     val = sum([int(j)**3 for j in getDigits(i)])
     if not findZeros(i) and val**(1/2) == int(val**(1/2)):
          cubeSumIsSquare.append(i)

leftTetrisOptions = []
rightTetrisOptions = []
for n in range(1000,10000):
     if not findZeros(n):
          a,b,c,d = getDigits(n)
          if convert(a,b) - convert(c,d) == convert(b,c):
               leftTetrisOptions.append(n)
          if convert(c,d) - convert(a,b) == convert(b,c):
               rightTetrisOptions.append(n)
