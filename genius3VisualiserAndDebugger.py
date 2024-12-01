import pygame

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

COLOURS = [(255,255,255),(255,0,0),(255,127,0),(255,255,0),(127,255,0),(0,255,255),(0,127,255),(127,0,255),(255,0,255),(255,0,127)]

cell_size = 130


grid ="""666688
333100
053722
955772
954470
904400
""".splitlines()
grid = [list(line) for line in grid]

#Uncomment line 26 to edit the empty crossnumber
#grid = [["" for _ in range(6)] for _ in range(6)]

cluePoints = [[(0,0),(20,12)],[(0,2),(23,0)],[(0,3),(17,0)],[(0,4),(18,6)],[(0,5),(19,0)],[(1,0),(0,9)],[(1,3),(0,1)],[(2,1),(16,0)],[(2,2),(0,3)],[(2,3),(24,0)],[(2,4),(13,2)],[(3,0),(22,18)],[(3,2),(0,5)],[(3,5),(19,0)],[(4,1),(15,4)],[(4,2),(14,0)],[(4,3),(0,10)],[(5,0),(0,7)],[(5,2),(0,11)]]

verticalBars = ["|   | |", "|  | ||", "||| | |", "| | |||", "|| |  |", "| |   |"]
horizontalBars = ["------"," -    "," - -- ","-    -"," -- - ","    - ","------"]

font_path = "Montserrat-Light.ttf"
font = pygame.font.Font(font_path, int(cell_size/2))
fontSmaller = pygame.font.Font(font_path, int(cell_size/5))

borders = [
    [(0, 0)] 
]

rows = len(grid)
cols = len(grid[0])
width = cols * cell_size
height = rows * cell_size


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Genius 3")

def draw_grid():
    for row in range(rows):
        for col in range(cols):
            rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, COLOURS[int(grid[row][col])], rect)
            pygame.draw.rect(screen, BLACK, rect, 1)

            if grid[row][col] != "":
                text = font.render(grid[row][col], True, BLACK)
                text_rect = text.get_rect(center=rect.center)
                screen.blit(text, text_rect)

    for (a,b),(c,d) in cluePoints:
        res = ""
        
        lilrectac = pygame.Rect(b * cell_size, a * cell_size, cell_size, cell_size/3)

        if c != 0:
            res += f"{c}↓  "
        if d != 0:
            res += f"{d} →"
        text = fontSmaller.render(res, True, BLACK)
        text_rect = text.get_rect(center=lilrectac.center)
        screen.blit(text, text_rect)

    for row in range(len(verticalBars)):
         for col in range(len(verticalBars[row])):
            if verticalBars[row][col] == "|":
                
                col -= 1
                start_pos = (col * cell_size + cell_size, row * cell_size)
                end_pos = (col * cell_size + cell_size, row * cell_size + cell_size)
                pygame.draw.line(screen, BLACK, start_pos, end_pos, 8)
                col += 1

    for row in range(len(horizontalBars)):
         for col in range(len(horizontalBars[row])): 

               
            if horizontalBars[row][col] == "-":
                
                row -= 1
                start_pos = (col * cell_size, row * cell_size + cell_size)
                end_pos = (col * cell_size + cell_size, row * cell_size + cell_size)
                pygame.draw.line(screen, BLACK, start_pos, end_pos, 8)
                row += 1


def placeNumber(pNumber, start_pos, direction):    
    row, col = start_pos
    if direction == "a":
        for i in range(len(pNumber)):
            if col + i < cols:
                grid[row][col + i] = pNumber[i]
    elif direction == "d":
        for i in range(len(pNumber)):
            if row + i < rows:
                grid[row + i][col] = pNumber[i]
        
running = True

number = ""
start_pos = (0, 0)
direction = "a"

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            start_pos = (pos[1] // cell_size, pos[0] // cell_size)
            number = input("number: ")
            direction = input("Direction (a/d): ").lower()

            placeNumber(number, start_pos, direction)
    screen.fill(BLACK)
    draw_grid()
    pygame.display.flip()
