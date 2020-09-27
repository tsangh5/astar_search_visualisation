import pygame
import math
import random
import sys
import itertools
start_node = [500, 500]
coordinates = [i for  i in range(10, 490, 20)]
possible_nodes = []
for pair in itertools.product(coordinates, repeat=2):
    possible_nodes.append(pair)
blocks = []
neighbours = []
f_list = []
path = []
for i in range(0, 2):
    blocks.append(pygame.Rect(random.choice(coordinates), random.choice(coordinates), 20, 20))
for block in blocks:
    if block.x + block.y < start_node[0] + start_node[1]:
        start_node = [block.x, block.y]
for block in blocks:
    if block != start_node:
        goal = block
def find_neighbours(current_node):
    for node in possible_nodes:
        if abs(node[0] - current_node[0]) == 10 or abs(node[1]- current_node[1]) == 10:
            neighbours.append(node)
def f(neighbour, last, current_node):
    g = last[2] + cost(current_node)
    h = math.sqrt(pow(goal[1] - neighbour[1], 2)+pow(goal[0]-neighbour[0]))
    f = g+h
    f_list.append([neighbour, f, g, h])
def best_node():
    best_node = f_list[0]
    for node in f_list:
        if node[1] < x[1]:
            best_node = node
    return best_node
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
GREEN = (50,205,50)
WINDOW_HEIGHT = 500
WINDOW_WIDTH = 500
GOLD = (255,215,0)
def find_path():
    global neighbours
    current_node = start_node
    while current_node != goal:
        find_neighbours(current_node)
        for neighbour in neighbours:
            f(neighbour, start_node, current_node)
            best_node()
            path.append(best_node)
            current_node = best_node
        neighbours = []
        f_list = []
    
def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)
    find_path()
    while True:
        drawGrid()
        drawBlocks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


def drawGrid():
    blockSize = 20 #Set the size of the grid block
    for x in range(WINDOW_WIDTH):
        for y in range(WINDOW_HEIGHT):
            rect = pygame.Rect(x*blockSize, y*blockSize,
                               blockSize, blockSize)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)
def drawBlocks():
    for block in blocks:
        if [block.x, block.y] == [start_node[0], start_node[1]]:
            pygame.draw.rect(SCREEN, GREEN, block, 0)
        else:
            pygame.draw.rect(SCREEN, GOLD, block, 0)
def drawPath():
    for block in path:
        pygame.draw.rect(SCREEN, GREEN, block, 0)

if __name__ == "__main__":
    main()