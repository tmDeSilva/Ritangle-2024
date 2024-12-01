import math
from itertools import permutations
from functools import lru_cache
import time

#Get a list  of what numbers have a particular digit for a specific column 
# (e.g. numbers with '9' for the tens digit are grouped together)
def getSetList(pList, column):

     res = [set() for _ in range(10)]
     for n in pList:
          if '0' not in str(n):
               res[int(str(n)[-column])] |= {n}

     return res

#1ac, 3ac, 6ac
#Between them is a cube, a lucky number and a happy number
cubes = [n ** 3 for n in range(math.ceil(100**(1/3)), math.floor(1000**(1/3))+1)]

I = 1
remaining = [int(i) for i in range(1,1000,2)]
while I < len(remaining):
     toRemove = set()
     #The step 'remaining[I]' creates the sieve that allows the remaining 
     # numbers to be filtered down to the final lucky numbers
     for i in range(remaining[I] - 1, len(remaining),remaining[I]):
          toRemove |= {remaining[i]}

     remaining = sorted(set(remaining) - toRemove)
     I += 1

luckyNumbers = [n for n in remaining if 100 <= n and n < 1000]

#A recursive function allows us to find happy numbers by checking if a 
# number ever reaches the base case '1' when continuously applying the operation
# that sums the squares of the digits
def is_happy(n,s = set()):
     if n == 1:
          return True
     if n in s:
          return False
     return is_happy(sum([(int(i))**2 for i in str(n)]), s | {n})

happyNumbers = [n for n in range(100,1000) if is_happy(n)]

#Check if a number is prime
@lru_cache(maxsize=None)
def is_prime(n): 
    if n <= 1: 
        return False 
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False 
    return True 



#2dn, 6dn
fourDigitPrimes = []
for i in range(1000,10000):
     if is_prime(i):
          fourDigitPrimes.append(i)

fourDigitPrimesUnits = getSetList(fourDigitPrimes, 1)
fourDigitPrimesTens = getSetList(fourDigitPrimes, 2)
fourDigitPrimesHundreds = getSetList(fourDigitPrimes, 3)
fourDigitPrimesThousands = getSetList(fourDigitPrimes, 4)
#12ac
cullen = [161,385,897] #3Digit Cullen numbers
#15ac
lucas = [123,199,322,521,843] #3Digit Lucas numbers

#10ac, 16ac
#'Divisorable' numbers are those which are divisible 
# by the total number of factors they have (including 1 and itself)
divisorable = []
for pN in range(100,1000):
    T = set()
    for iN in range(1,math.ceil(pN ** (1/2))+1):
            if pN%iN == 0:
                T |= {iN, pN//iN}

    if pN % len(T) == 0:
         divisorable.append(pN)

divisorablesUnits = getSetList(divisorable, 1)
divisorablesHundreds = getSetList(divisorable, 3)


#19ac, 20ac, 21ac
fibonacci = [144,233,377,610,987] #3Digit fibonacci numbers
squares = [n**2 for n in range(10,32)] #Square numbers between 100 and 961
triangular = [n * (n+1) // 2 for n in range(int((-1/2 + (2 * 100) + 1/4)**(1/2)),int((-1/2 + (2 * 1000) + 1/4)**(1/2))+1)]

#The crossnumber as a set of strings
numberSoup = """1 # 2 3 4 5 6 # 7
8 9 10 11 # 12 # 13 #
14 15 # # 16 # # 17 18
19 # # 20 # # 21 # #""".splitlines()

numberSoup = [line.split() for line in numberSoup]
coords = [(0,0) for i in range(21)]

#Get the positions of the clues
for i in range(len(numberSoup)):
    for j in range(len(numberSoup[i])):
        try:
            coords[int(numberSoup[i][j])-1] = (i,j)
            numberSoup[i][j] = "#"
        except:
            pass

#Check if every digit appears the same number of times
def digitsAppear4Times():
     L = []
     for row in numberSoup:
          L += row
     for i in range(1,10):
          if L.count(str(i)) != 4:
               return False
          
     return True

#Write an answer to its position
def write(number,direction,pos):
    global numberSoup
    string = str(number)
    coord = coords[pos-1]
    if direction == "dn":
        for i in range(coord[0],coord[0] + len(string)):
            numberSoup[i][coord[1]] = string[i - coord[0]]
    else:
        for j in range(coord[1],coord[1] + len(string)):
            numberSoup[coord[0]][j] = string[j - coord[1]]

#Get the answer to a clue
def getValue(length, direction, pos):
    coord = coords[pos-1]
    if direction == "dn":
        return convert([int(numberSoup[i][coord[1]]) for i in range(coord[0],coord[0] + length)])
    
    else:
        return convert([int(numberSoup[coord[0]][j]) for j in range(coord[1],coord[1] + length)])

#clear the crossnumber
def clear():
    global numberSoup
    numberSoup = [["#" for j in range(len(numberSoup[0]))] for i in range(len(numberSoup))]

#Print out the crossnumber
def display(sep = " "):
    for line in numberSoup:
        print(sep.join(line))

#Convert a list of digits to a denary number 
# (e.g. [1,2,3] -> 123)
def convert(l):
    T = 0
    for i in range(len(l)):
        T += l[i] * 10 ** (len(l) - 1 - i)
    return T


#Find all the harshad numbers below 1000
#5dn = 11dn - harshad
harshad = []
for i in range(1,1000):
     if i % sum([int(j) for j in str(i)]) == 0:
          harshad.append(i)

#Find all the four digit numbers whose sum of each digit cubed is a square 
cubeSumIsSquare = []
for i in range(1000,10000):
     val = sum([int(j)**3 for j in str(i)])
     if '0' not in str(i) and val**(1/2) == int(val**(1/2)):
          cubeSumIsSquare.append(i)

cubeSumIsSquareUnits = getSetList(cubeSumIsSquare,1)
cubeSumIsSquareThousands = getSetList(cubeSumIsSquare,4)


#8ac = 1dn - 9dn
tetris1 = []
#17ac = 18dn - 13dn
tetris2 = []
for n in range(1000,10000):
     if '0' not in str(n):
          a,b,c,d = [int(i) for i in str(n)]
          if convert([a,b]) - convert([c,d]) == convert([b,c]):
               tetris1.append(n)
          if -(convert([a,b]) - convert([c,d])) == convert([b,c]):
               tetris2.append(n)

tetris1Units = getSetList(tetris1, 1)
tetris1Thousands = getSetList(tetris1, 4)
tetris2Units = getSetList(tetris2, 1)
tetris2Thousands = getSetList(tetris2, 4)



#All top row digits are different as are the bottom row digits
topTuples = []
for a,b,c,d,e,f,g,h,i in permutations([i for i in range(1,10)],9):
     if convert([g,h,i]) in cubes:
          if convert([a,b,c]) in happyNumbers:
               if convert([d,e,f]) in luckyNumbers:
                    topTuples.append((convert([a,b,c]),convert([d,e,f]),convert([g,h,i])))

bottomTuples = []
for a,b,c,d,e,f,g,h,i in permutations([i for i in range(1,10)],9):
     if convert([g,h,i]) in fibonacci:
          if convert([a,b,c]) in squares:
               if convert([d,e,f]) in triangular:
                    bottomTuples.append((convert([a,b,c]),convert([d,e,f]),convert([g,h,i])))

#The resulting bottom row tuple (19ac, 20ac, 21ac) is (324,561,987) in some order
bottomTuple = bottomTuples[0]

#14dn is a divisor of the sum(19ac) + sum(20ac) + sum(21ac) 
# which is the 9th triangular number which is 45.
# as clues are non-trivial 14dn can only be 15 and so 19ac must be 561

a = 561
C = 0
initialTime = time.time()
for b,c in [(324,987),(987,324)]:
     #a: 19ac, b: 20ac, c:21ac
     for topTuple in topTuples:
          #d: 1ac, e: 3ac, f: 6ac
          for d,e,f in permutations(topTuple,3):
               write(a,"ac",19)
               write(b,"ac",20)
               write(c,"ac",21)

               write(d,"ac",1)
               write(e,"ac",3)
               write(f,"ac",6)

               write(15, "dn", 14)

               #x: 4dn
               #4dn's units = Tens of 20ac, 4dn's thousands = tens of 3ac
               for x in cubeSumIsSquareUnits[(b%100)//10].intersection(cubeSumIsSquareThousands[(e%100)//10]):
                    write(x,"dn",4)
                    #y: 10ac
                    #10ac's units = hundreds of 4dn
                    for y in divisorablesUnits[(x%1000)//100]:
                         write(y,"ac",10)
                         #cc: 15ac
                         for cc in cullen:
                              write(cc,"ac",15)
                              #p: 2dn
                              for p in fourDigitPrimesTens[(cc%100)//10].intersection(fourDigitPrimesHundreds[y//100]).intersection(fourDigitPrimesUnits[a%10]).intersection(fourDigitPrimesThousands[d%10]):
                                   #let the digits of t be A',B',C',D'
                                   # then r: 1dn: A'B', qr: 8ac: B'C',q: 9dn: C'D'
                                   for t in tetris1Units[cc//100].intersection(tetris1Thousands[d//100]):
                                        q = t%100
                                        r = (t-t%100)//100
                                        rq = r - q
                                        write(q,"dn",9)
                                        write(r, "dn",1)
                                        #1dn is a divisor of 20ac
                                        if b % r == 0:
                                             #z: 16ac
                                             for z in divisorablesHundreds[int(str(x)[2])]:
                                                  write(z,"ac",16)
                                                  if y != z:
                                                       #l: 12ac
                                                       for l in lucas:
                                                            write(l,"ac",12)
                                                            #p2: 6dn
                                                            #p2's digits: hundreds of 6ac, tens of 12ac, units of 16ac, hundreds of 21ac
                                                            p2 = convert([f//100, (l%100)//10, z%10, c//100])
                                                            if p2 in fourDigitPrimes:
                                                                 #u: 11dn
                                                                 #u's digits: tens of 10ac, units of 15ac, hundreds of 20ac
                                                                 #v: 5dn
                                                                 #v's digits: units of 3ac, hundreds of 12ac, tens of 16ac
                                                                 u = convert([(y%100)//10,cc%10,b//100])
                                                                 v = convert([e%10,l//100,(z%100)//10])

                                                                 #11dn - harshad = 5dn, 11dn - 5dn = harshad
                                                                 if (u - v) in harshad:

                                                                      #let the digits of t be A',B',C',D'
                                                                      # then g: 18dn: C'D', gh: 17ac: B'C',h: 13dn: A'B'
                                                                      for t2 in tetris2Thousands[l%10].intersection(tetris2Units[c%10]):

                                                                           #g: 18dn
                                                                           #h: 13dn
                                                                           g = t2%100
                                                                           h = (t2-t2%100)//100
                                                                           gh = g - h
                                                                           write(g, "dn",18)
                                                                           write(h , "dn",13)

                                                                           #:Last digit last
                                                                           #lastLast (now everybody go to breakfast): 7dn
                                                                           for last in range(1,10):
                                                                                #7dn's digits: units of 6ac and the last digit
                                                                                lastLast = convert([f%10,last])

                                                                                #check if 7dn is a prime divisor of 2ac
                                                                                #if e % lastLast == 0:
                                                                                     #if is_prime(e // lastLast):
                                                                                if is_prime(lastLast):
                                                                                     if e % lastLast == 0:
                                                                                          write(lastLast, "dn", 7)
                                                                                          
                                                                                          #Check if every digit only appears four times (hence the same number of times)
                                                                                          if digitsAppear4Times():
                                                                                               dnSolutions = [getValue(2,"dn",1),
                                                                                                              getValue(4,"dn",2),
                                                                                                              getValue(4,"dn",4),
                                                                                                              getValue(3,"dn",5),
                                                                                                              getValue(4,"dn",6),
                                                                                                              getValue(2,"dn",7),
                                                                                                              getValue(2,"dn",9),                                                                      
                                                                                                              getValue(3,"dn",11),                                                                                                             
                                                                                                              getValue(2,"dn",13),
                                                                                                              getValue(2,"dn",14),
                                                                                                              getValue(2,"dn",18)]
                                                                                               
                                                                                               acSolutions = [getValue(3,"ac",1),
                                                                                                              getValue(3,"ac",3),
                                                                                                              getValue(3,"ac",6),
                                                                                                              getValue(2,"ac",8),
                                                                                                              getValue(3,"ac",10),
                                                                                                              getValue(3,"ac",12),
                                                                                                              getValue(3,"ac",15),
                                                                                                              getValue(3,"ac",16),
                                                                                                              getValue(2,"ac",17),
                                                                                                              getValue(3,"ac",19),
                                                                                                              getValue(3,"ac",20),
                                                                                                              getValue(3,"ac",21)]
                                                                                               
                                                                                               print(f"Difference D: {abs(sum(acSolutions) - sum(dnSolutions))}\n")
                                                                                               print("Crossnumber: Number Soup")
                                                                                               display("")
                                                                                               C += 1

print(f"Number of solutions found: {C}")
print(f"Time taken {time.time() - initialTime:.2f}s")
