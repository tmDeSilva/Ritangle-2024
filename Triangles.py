from itertools import permutations
from functools import lru_cache
import time

@lru_cache(maxsize=None)
def is_prime(n): 
    if n <= 1: 
        return False 
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False 
    return True 

def hcf(x, y):
    while y:
         x, y = y, x % y
    return x
triples = set()
for a in range(1,1000):
    for b in range(1,1000):
        if a**2 + b**2 < 1000 and a**2 - b**2 != 0:
            if hcf(abs(a**2 - b**2), abs(2*a*b)) == 1:
                triples |= {tuple(sorted([abs(a**2 - b**2),abs(2*a*b), a**2 + b**2]))}

triplesList = sorted(list(triples))

triangles = """1 # 2 3 4 5
6 7 # 8 9 #
10 # 11 # # 12
13 # # 14 # #""".splitlines()

triangles = [line.split() for line in triangles]
coords = [(0,0) for i in range(14)]

for i in range(len(triangles)):
    for j in range(len(triangles[i])):
        try:
            coords[int(triangles[i][j])-1] = (i,j)
            triangles[i][j] = "#"
        except:
            pass

def clearTriangles():
    global triangles
    triangles = [["#" for j in range(len(triangles[0]))] for i in range(len(triangles))]

def convert(pList):
    result = 0
    for i in range(len(pList)):
        result += pList[i] * 10 ** (len(pList) - 1 - i)
    return result

def write(number,direction,pos):
    global triangles
    string = str(number)
    coord = coords[pos-1]
    if direction == "dn":
        for i in range(coord[0],coord[0] + len(string)):
            triangles[i][coord[1]] = string[i - coord[0]]
    else:
        for j in range(coord[1],coord[1] + len(string)):
            triangles[coord[0]][j] = string[j - coord[1]]

def getValue(length, direction, pos):
    coord = coords[pos-1]
    if direction == "dn":
        return convert([int(triangles[i][coord[1]]) for i in range(coord[0],coord[0] + length)])
    else:
        return convert([int(triangles[coord[0]][j]) for j in range(coord[1],coord[1] + length)])

def display(sep = " "):
    for line in triangles:
        print(sep.join(line))

#Pythagorean triples of these forms
twoTwoTwo = []
twoThreeThree = []

for a,b,c in triplesList:
    if a > 9 and b > 9 and c > 9:
        if a//100 == 0 and b//100 == 0 and c//100 == 0:
            twoTwoTwo.append((a,b,c))
        elif a//100 == 0 and b//100 > 0 and c//10 > 0:
            twoThreeThree.append((a,b,c))

#Find possible values for 1ac, 2ac and 4ac
coprimeCompositeTriangles = set()
for i in range(11,101,2):
    for j in range(11,101,2):
        for k in range(11,101,2):
            L = sorted([i,j,k])
            a,b,c = L
            if a + b > c:
                if not(is_prime(a)) and not(is_prime(b)) and not(is_prime(c)):
                    if hcf(a,b) == 1 and hcf(b,c) == 1 and hcf(a,c):
                        val = -1/2 + ((2 * (a+b+c)) + 1/4)**(1/2)
                        if int(val) == val:   
                            coprimeCompositeTriangles |= {(a,b,c)}

#13ac,7dn,1dn 
#14ac,9dn,5dn 
possible233 = []
for a,b,c in twoThreeThree:
    if b % 10 == (c % 100)//10:
        possible233.append((a,b,c))

for a,b,c in twoThreeThree:
    if c % 10 == (b % 100)//10:
        possible233.append((a,c,b))

C = 0
initialTime = time.time()
for a,b,c in possible233:
    for d,e,f in possible233:
        if (a,b,c) != (d,e,f):
            for triple in twoTwoTwo:
                for x,y,z in permutations(triple ,3):
                    if (x%10 == c // 100) and(y % 10 == (f%10)):
                        for triple2 in coprimeCompositeTriangles:
                            for u,v,w in permutations(triple2, 3):
                                if (u//10 == a//10) and (v%10 == d//10):
                                    for n in range(10, 99):
                                        d1, d2 = [int(e) for e in str(n)]
                                        if d2 != 0:
                                            r = convert([w // 10,d1,z//10])
                                            s = convert([w % 10,d2,z%10])
                                            
                                            
                                            clearTriangles()        
                                            write(c, "ac", 13)
                                            write(b, "dn", 7)
                                            write(a, "dn", 1)
                                           
                                            write(f, "ac", 14)
                                            write(e, "dn", 9)                                            
                                            write(d, "dn", 5)
 
                                            write(x, "dn", 10)                                            
                                            write(y, "dn", 12)                                            
                                            write(z, "ac", 11)

                                            write(u, "ac", 1)                                            
                                            write(v, "ac", 4)                                            
                                            write(w, "ac", 2)
                                           
                                            write(r, "dn", 2)                                            
                                            write(s, "dn", 3)
                                        
                                            
                                            if (r+s)**(1/2) == int((r+s)**(1/2)):
                                                p = getValue(3, "ac", 6)
                                                q = getValue(3, "ac", 8)

                                                questionAblesolutions = [getValue(2, "dn", 8),getValue(2, "ac", 7),getValue(2, "ac", 9)]

                                                solutions = [a,b,c,d,e,f,x,y,z,u,v,w,r,s,p,q]
                                                
                                                flag = False
                                                for i in range(len(solutions)-1):
                                                    for j in range(i+1,len(solutions)):
                                                        if abs(solutions[i] - solutions[j]) == sum([u,v,w]):      
                                                            flag = True

                                                if flag:
                                                    dnSolutions = [getValue(2,"dn",1),
                                                                   getValue(3,"dn",2),
                                                                   getValue(3,"dn",3),
                                                                   getValue(2,"dn",5),
                                                                   getValue(3,"dn",7),
                                                                   getValue(3,"dn",9),
                                                                   getValue(2,"dn",10),
                                                                   getValue(2,"dn",12)]
                                                    
                                                    acSolutions = [getValue(2,"ac",1),
                                                                   getValue(2,"ac",2),
                                                                   getValue(2,"ac",4),
                                                                   getValue(3,"ac",6),
                                                                   getValue(3,"ac",8),
                                                                   getValue(2,"ac",11),
                                                                   getValue(3,"ac",13),
                                                                   getValue(3,"ac",14)]
                                                    
                                                    print(f"Difference D: {abs(sum(acSolutions) - sum(dnSolutions))}\n")

                                                    print("Crossnumber: Triangles")
                                                    display("")

                                                    C += 1
                                            
print(f"Number of solutions found: {C}")
print(f"Time taken {time.time() - initialTime:.2f}s")
