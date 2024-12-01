#Reprsentation of the empty crossnumber puzzle
lines="""
# # # #|# #|
--=--------|
# # #|# #|#|
--=---===--|
#|#|# #|# #|
=---------=|
# #|# #|#|#|
--===---=--|
#|# #|# # #|
--------=--|  
# #|# # # #|
===========|

""".splitlines()[1:-1]

grid = []
for i in range(0,len(lines),2):
    row = []
    sepRow = []
    for j in range(len(lines[i])):

        e =  lines[i][j]
        e2 = lines[i+1][j]

        if e == "#":
            sepRow.append(e2*2)
            row.append([[e,e]]*2)
        else:
            row.append(e)
            sepRow.append(e2)
    grid.append(row)
    grid.append(sepRow)


acCoords = []
for i in range(0,6):
    J = 0
    while J < 6:
        length = 1
        while grid[2*i][2*J + 1] != "|":
            length += 1
            J += 1
        J += 1
        if length > 1:
            acCoords.append((length,J-length,i))

dnCoords = []
for j in range(0,6):
    I = 0
    while I < 6:
        length = 1
        while grid[2*I + 1][2*j] != "==":
            length += 1
            I += 1
        I += 1
        if length > 1:
            dnCoords.append((length,j, I - length))

acCoords = sorted(acCoords)
dnCoords = sorted(dnCoords)


grid ="""666688
333100
053722
955772
954470
904400
""".splitlines()

def convert(l):
    T = 0
    for i in range(len(l)):
        T += l[i] * 10 ** (len(l) - 1 - i)
    return T

grid = [[int(i) for i in line] for line in grid]

acT = 0
for a,b,c in acCoords:
    acT += convert(grid[c][b:b+a])

dnT = 0
for a,b,c in dnCoords:
    dnT += convert([grid[c+ i][b] for i in range(a)])

print(f"Difference D: {abs(dnT- acT)}\n")

for line in grid:
    print("".join([str(e) for e in line]))
