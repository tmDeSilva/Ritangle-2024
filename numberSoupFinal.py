import math
import time
from itertools import permutations
import numberBank as nb

convert = nb.convert
isprime = nb.is_prime

class Number:
    def __init__(self, cNumber=0):
        self.number = cNumber
        
        digits = self.padWithZeros(self.getDigits(self.number))
        self.thousands = digits[0]
        self.hundreds = digits[1]
        self.tens = digits[2]
        self.units = digits[3]
        
    def getDigits(self,pNumber):
            result = []

            while pNumber != 0:
                result.append(pNumber % 10)
                pNumber = (pNumber - pNumber % 10) // 10

            return result[::-1]
    
    def padWithZeros(self,pDigitList):
         return [0] * (4 - len(pDigitList)) + pDigitList
    
    def changeNumber(self,newNumber):
         self.__init__(newNumber)
          
class AnswerList:
    def __init__(self, cList):
        self.LIST = cList
        self.numbersByDigits = [[set() for _ in range(10)] for _ in range(len(self.getDigits(self.LIST[0])))]

        for iNumber in self.LIST:
             iDigits = self.getDigits(iNumber)
             for i in range(len(iDigits)):
                  self.numbersByDigits[i][iDigits[i]] |= {iNumber}

    def getDigits(self,pNumber):
        result = []

        while pNumber != 0:
            result.append(pNumber % 10)
            pNumber = (pNumber - pNumber % 10) // 10

        return result[::-1]
    
    def getPossibleValues(self,*args):
 
         validSets = []
         for i in range(len(args)):
              if args[i] != "?":
                   validSets.append(self.numbersByDigits[i][args[i]])

         possibleValues = set()
         if set() in validSets:
              return set()
         
         for iSet in validSets:
              if len(possibleValues) == 0:
                   possibleValues = iSet
              else:
                   possibleValues = possibleValues.intersection(iSet)
         return possibleValues

class Crossnumber:
    def __init__(self,crossnumberString):
        self.crossnumber = [line.split() for line in crossnumberString.splitlines()]
        numbers = []
        for i in range(len(self.crossnumber)):
            for j in range(len(self.crossnumber[i])):
                if self.crossnumber[i][j].isdigit():
                        numbers.append(int(self.crossnumber[i][j]))

        self.coords = [(0,0) for i in range(max(numbers))]

        for i in range(len(self.crossnumber)):
            for j in range(len(self.crossnumber[i])):
                if self.crossnumber[i][j].isdigit():
                    self.coords[int(self.crossnumber[i][j])-1] = (i,j)
                    
        self.clear()

    def clear(self):
        for i in range(len(self.crossnumber)):
            for j in range(len(self.crossnumber[i])):
                self.crossnumber[i][j] = "#"

    def write(self,number,direction,pos):
        string = str(number)
        coord = self.coords[pos-1]
        if direction == "dn":
            for i in range(coord[0],coord[0] + len(string)):
                self.crossnumber[i][coord[1]] = string[i - coord[0]]
        else:
            for j in range(coord[1],coord[1] + len(string)):
                self.crossnumber[coord[0]][j] = string[j - coord[1]]

    def getValue(self,length, direction, pos):
        coord = self.coords[pos-1]
        if direction == "dn":
            return convert(*[int(self.crossnumber[i][coord[1]]) for i in range(coord[0],coord[0] + length)])
        else:
            return convert(*[int(self.crossnumber[coord[0]][j]) for j in range(coord[1],coord[1] + length)])
        
    def display(self,sep=" "):
        for line in self.crossnumber:
            print(sep.join(line))
        print()

    def digitsAppear4Times(self):
        pCountList = []
        for row in self.crossnumber:
            pCountList += row
        for i in range(1,10):
            if pCountList.count(str(i)) != 4:
                return False
        return True

numberSoup = Crossnumber("""1 # 2 3 4 5 6 # 7
                            8 9 10 11 # 12 # 13 #
                            14 15 # # 16 # # 17 18
                            19 # # 20 # # 21 # #""")
#Lists of number

#1ac, 3ac, 6ac : 3 digit
cubesList = AnswerList(nb.cubes)
happyNumbersList = AnswerList(nb.happyNumbers)
luckyNumbersList = AnswerList(nb.luckyNumbers)
#2dn, 6dn : 4 digit
fourDigitPrimesList = AnswerList(nb.fourDigitPrimes)
#12ac : 3 digit
lucasNumbersList = AnswerList(nb.lucasNumbers)
#15ac : 3 digit
cullenNumbersList = AnswerList(nb.cullenNumbers)
#10ac, 16ac : 3 digit
divisorableList = AnswerList(nb.divisorable)
#19ac, 20ac, 21ac : 3 digit
fibonacciNumbersList = AnswerList(nb.fibonacciNumbers)
triangularList = AnswerList(nb.triangular)
squaresList = AnswerList(nb.squares)
#5dn = 11dn - harshad : 3 digit
harshadList = nb.harshad
#4dn : 4 digit
cubeSumIsSquareList = AnswerList(nb.cubeSumIsSquare)
#1dn, 9dn, 8ac = 1dn - 9dn : 2 digit
leftTetrisList = AnswerList(nb.leftTetrisOptions)
#13dn, 18dn, 17ac = 18dn - 13dn : 2 digit
rightTetrisList = AnswerList(nb.rightTetrisOptions)



#All top row digits are different as are the bottom row digits
topTuples = []
for a,b,c,d,e,f,g,h,i in permutations([i for i in range(1,10)],9):
     if convert(g,h,i) in cubesList.LIST:
          if convert(a,b,c) in happyNumbersList.LIST:
               if convert(d,e,f) in luckyNumbersList.LIST:
                    topTuples.append((convert(a,b,c),convert(d,e,f),convert(g,h,i)))

bottomTuples = []
for a,b,c,d,e,f,g,h,i in permutations([i for i in range(1,10)],9):
     if convert(g,h,i) in fibonacciNumbersList.LIST:
          if convert(a,b,c) in squaresList.LIST:
               if convert(d,e,f) in triangularList.LIST:
                    bottomTuples.append((convert(a,b,c),convert(d,e,f),convert(g,h,i)))

#The resulting bottom row tuple (19ac, 20ac, 21ac) is (324,561,987) in some order
bottomTuple = bottomTuples[0]

#14dn is a divisor of the sum(19ac) + sum(20ac) + sum(21ac) 
# which is the 9th triangular number which is 45.
# as clues are non-trivial 14dn can only be 15 and so 19ac must be 561

#Across numbers
_1acNumber = Number()
_3acNumber = Number()
_6acNumber = Number()
_8acNumber = Number()
_10acNumber = Number()
_12acNumber = Number()
_15acNumber = Number()
_16acNumber = Number()
_17acNumber = Number()
_19acNumber = Number()
_20acNumber = Number()
_21acNumber = Number()

#Down numbers
_1dnNumber = Number()
_2dnNumber = Number()
_4dnNumber = Number()
_5dnNumber = Number()
_6dnNumber = Number()
_7dnNumber = Number()
_9dnNumber = Number()
_11dnNumber = Number()
_13dnNumber = Number()
_14dnNumber = Number()
_18dnNumber = Number()


_19ac = 561
_19acNumber.changeNumber(_19ac)
_14dn = 15
_14dnNumber.changeNumber(_14dn)
solutionsCount = 0

initialTime = time.time()
for _20ac,_21ac in [(324,987),(987,324)]:
     _20acNumber.changeNumber(_20ac)
     _21acNumber.changeNumber(_21ac)
    
     for topTuple in topTuples:
          
          for _1ac,_3ac,_6ac in permutations(topTuple,3):
               _1acNumber.changeNumber(_1ac)
               _3acNumber.changeNumber(_3ac)
               _6acNumber.changeNumber(_6ac)

               numberSoup.write(_19ac,"ac",19)
               numberSoup.write(_20ac,"ac",20)
               numberSoup.write(_21ac,"ac",21)

               numberSoup.write(_1ac,"ac",1)
               numberSoup.write(_3ac,"ac",3)
               numberSoup.write(_6ac,"ac",6)

               numberSoup.write(15, "dn", 14)

               
               for _4dn in cubeSumIsSquareList.getPossibleValues(_3acNumber.tens,"?","?",_20acNumber.tens):
                    _4dnNumber.changeNumber(_4dn)
                    numberSoup.write(_4dn,"dn",4)
                    
                    for _10ac in divisorableList.getPossibleValues("?","?",_4dnNumber.hundreds):
                         _10acNumber.changeNumber(_10ac)
                         numberSoup.write(_10ac,"ac",10)
                         
                         for _15ac in cullenNumbersList.LIST:
                              _15acNumber.changeNumber(_15ac)
                              numberSoup.write(_15ac,"ac",15)
                              
                              
                              for _2dn in fourDigitPrimesList.getPossibleValues(_1acNumber.units,
                                                                                _10acNumber.hundreds,
                                                                                _15acNumber.tens,
                                                                                _19acNumber.units):
                                   _2dnNumber.changeNumber(_2dn)
                                   
                                   for _1dn8ac9dn in leftTetrisList.getPossibleValues(_1acNumber.hundreds,"?","?",_15acNumber.hundreds):
                                        
                                        _9dn = _1dn8ac9dn%100
                                        _1dn = (_1dn8ac9dn-_1dn8ac9dn%100)//100
                                        _8ac = _1dn - _9dn

                                        _9dnNumber.changeNumber(_9dn)
                                        _1dnNumber.changeNumber(_1dn)
                                        _8acNumber.changeNumber(_8ac)

                                        numberSoup.write(_9dn,"dn",9)
                                        numberSoup.write(_1dn, "dn",1)
                                        
                                        if _20ac % _1dn == 0:
                                             
                                             for _16ac in divisorableList.getPossibleValues(_4dnNumber.tens,"?","?"):
                                                  _16acNumber.changeNumber(_16ac)
                                                  numberSoup.write(_16ac,"ac",16)
                                                  if _10ac != _16ac:
                                                       
                                                       for _12ac in lucasNumbersList.LIST:
                                                            _12acNumber.changeNumber(_12ac)
                                                            numberSoup.write(_12ac,"ac",12)
                                                            
                                                            _6dn = convert(_6acNumber.hundreds,
                                                                             _12acNumber.tens,
                                                                             _16acNumber.units,
                                                                             _21acNumber.hundreds)
                                                            
                                                            _6acNumber.changeNumber(_6ac)
                                                            if _6dn in fourDigitPrimesList.LIST:
                                                                 
                                                                 _11dn = convert(_10acNumber.tens,_15acNumber.units,_20acNumber.hundreds)
                                                                 _5dn = convert(_3acNumber.units,_12acNumber.hundreds,_16acNumber.tens)
                                                                 
                                                                 _11dnNumber.changeNumber(_11dn)
                                                                 _5dnNumber.changeNumber(_5dn)
                                                                 
                                                                 if (_11dn - _5dn) in harshadList:
                                                                     
                                                                      for _13dn17ac18dn in rightTetrisList.getPossibleValues(_12ac%10,"?","?",_21ac%10):
                                    
                                                                           _18dn = _13dn17ac18dn%100
                                                                           _13dn = (_13dn17ac18dn-_13dn17ac18dn%100)//100
                                                                           _17ac = _18dn - _13dn

                                                                           _18dnNumber.changeNumber(_18dn)
                                                                           _13dnNumber.changeNumber(_13dn)
                                                                           _17acNumber.changeNumber(_17ac)

                                                                           numberSoup.write(_18dn, "dn",18)
                                                                           numberSoup.write(_13dn , "dn",13)

                                                                           for lastDigit in range(1,10):
                                                                        
                                                                                _7dn = convert(_6acNumber.units,lastDigit)
                                                                                _7dnNumber.changeNumber(_7dn)

                                                                                if isprime(_7dn):
                                                                                     if _3ac % _7dn == 0:
                                                                                          numberSoup.write(_7dn, "dn", 7)

                                                                                          if numberSoup.digitsAppear4Times():
                                                                                               dnSolutions = [_1dn,
                                                                                                              _2dn,
                                                                                                              _4dn,
                                                                                                              _5dn,
                                                                                                              _6dn,
                                                                                                              _7dn,
                                                                                                              _9dn,                                                                      
                                                                                                              _11dn,                                                                                                             
                                                                                                              _13dn,
                                                                                                              _14dn,
                                                                                                              _18dn]
                                                                                                                
                                                                                               acSolutions = [_1ac,
                                                                                                              _3ac,
                                                                                                              _6ac,
                                                                                                              _8ac,
                                                                                                              _10ac,
                                                                                                              _12ac,
                                                                                                              _15ac,
                                                                                                              _16ac,
                                                                                                              _17ac,
                                                                                                              _19ac,
                                                                                                              _20ac,
                                                                                                              _21ac]
                                                                                               
                                                                                               print(f"Difference D: {abs(sum(acSolutions) - sum(dnSolutions))}\n")
                                                                                               print("Crossnumber: Number Soup")
                                                                                               numberSoup.display("")
                                                                                               solutionsCount += 1

print(f"Number of solutions found: {solutionsCount}")
print(f"Time taken to solve number soup {time.time() - initialTime:.2f}s")
