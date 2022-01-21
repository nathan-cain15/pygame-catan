import math
import pygame
import random
from classes import Tile
from classes import Vertice

pygame.init()
root = pygame.display.set_mode((900, 600))

lightGreen = (81, 125, 25)
darkGreen = (55, 75, 30)
blue = (79, 166, 235)
yellow = (240, 173, 0)
red = (156, 67, 0)
grey = (123, 111, 131)
tan = (243, 192, 114)
white = (249, 238, 225)


def getPoints(tiltAngle, x, y, radius):
    pts = []
    for i in range(6):
        x = x + radius * math.cos(tiltAngle + math.pi * 2 * i / 6)
        y = y + radius * math.sin(tiltAngle + math.pi * 2 * i / 6)
        pts.append([int(x), int(y)])
    return pts

def randomColors(numOfLightGreen, numOfDarkGreen, numOfRed, numOfYellow, numOfGrey, numOfTan):

    lst = []

    for i in range(numOfLightGreen):
        lst.append(lightGreen)
    for i in range(numOfDarkGreen):
        lst.append(darkGreen)
    for i in range(numOfRed):
        lst.append(red)
    for i in range(numOfYellow):
        lst.append(yellow)
    for i in range(numOfGrey):
        lst.append(grey)
    for i in range(numOfTan):
        lst.append(tan)

    randomList = []

    for i in range(len(lst)):
        randomColor = random.choice(lst)
        lst.remove(randomColor)
        randomList.append(randomColor)
    return randomList

def generateNumbers(tiles):
    numbers = [5, 10, 8, 2, 9, 3, 4, 6, 11, 6, 11, 3, 4, 5, 12, 8, 10, 9]

    for tile in tiles:
        if tile.color == (243, 192, 114):
            desertPos = tiles.index(tile)

    num = numbers.index(random.choice(numbers))

    for tile in tiles:
        if tiles.index(tile) != desertPos:
            tile.number = numbers[num]
            if num == 17:
                num = 0
                continue
            num += 1
    return tiles


def makeMap(x, y, sideLength):
    tiles = []
    tile = [x, y]
    vertices = []
    edges = []
    num = 0
    for i in range(5):
        tiles.append(tile)
        points = getPoints(11, tile[0], tile[1], sideLength)
        for point in points:
            if point not in vertices:
                vertices.append(point)
        if num >= 2:
            if [points[5], points[0]] not in edges:
                edges.append([points[5], points[0]])
            for j in range(5):
                if [points[j], points[j+1]] not in edges:
                    edges.append([points[j], points[j+1]])

        tile = points[3]
        num += 1

    points = getPoints(11, tiles[0][0], tiles[0][1], sideLength)
    tile = [points[4][0], points[4][1] + sideLength]
    del tiles[0:2]
    del vertices[0:8]
    num = 0
    for i in range(5):
        tiles.append(tile)
        points = getPoints(11, tile[0], tile[1], sideLength)
        for point in points:
            if point not in vertices:
                vertices.append(point)
        if num >= 1:
            if [points[5], points[0]] not in edges:
                edges.append([points[5], points[0]])
            for j in range(5):
                if [points[j], points[j+1]] not in edges:
                    edges.append([points[j], points[j+1]])

        tile = points[3]
        num += 1
    points = getPoints(11, tiles[3][0], tiles[3][1], sideLength)
    tile = [points[4][0], points[4][1] + sideLength]
    tiles.remove(tiles[3])
    del vertices[17:24]
    for i in range(5):
        tiles.append(tile)
        points = getPoints(11, tile[0], tile[1], sideLength)
        for point in points:
            if point not in vertices:
                vertices.append(point)
        tile = points[3]

    points = getPoints(11, tiles[7][0], tiles[7][1], sideLength)
    tile = [points[4][0], points[4][1] + sideLength]
    for i in range(4):
        tiles.append(tile)
        points = getPoints(11, tile[0], tile[1], sideLength)
        for point in points:
            if point not in vertices:
                vertices.append(point)
        tile = points[3]

    points = getPoints(11, tiles[12][0], tiles[12][1], sideLength)
    tile = [points[4][0], points[4][1] + sideLength]
    for i in range(3):
        tiles.append(tile)

        points = getPoints(11, tile[0], tile[1], sideLength)
        for point in points:
            if point not in vertices:
                vertices.append(point)
        tile = points[3]

    colors = randomColors(4, 4, 3, 4, 3, 1)
    tilesList = []
    verticeList = []
    number = 0
    for tile in tiles:
        tilesList.append(Tile(colors[number], tile[0], tile[1], 1))
        number += 1
    tilesList = generateNumbers(tilesList)
    print(edges)
    for i in vertices:
        verticeList.append(Vertice(i[0], i[1]))
    return tilesList, verticeList, edges

def drawTiles(tiles, sideLength):
    for i in tiles:
        i.draw(root, i.color, 11, i.x, i.y, sideLength)

def drawVertices(vertices):
    for i in vertices:
        pygame.draw.rect(root, white, (i.x-5, i.y-5, 10, 10))

def drawEdges(edges):
    for edge in edges:
        pygame.draw.polygon(root, white, ((edge[0][0] - 3, edge[0][1]),  (edge[1][0] - 3, edge[1][1]), (edge[1][0] + 3, edge[1][1]), (edge[0][0] + 3, edge[0][1])))

def drawNumbers(tiles, sidelength):
    diagonal = math.sqrt(3) * sidelength
    myfont = pygame.font.SysFont('Comic Sans MS', 20)
    for tile in tiles:
        if tile.number == 1:
            continue
        num = str(tile.number)
        textsurface = myfont.render(num, False, (0, 0, 0))
        root.blit(textsurface, (tile.x + (diagonal/2 - 5), tile.y - sidelength + 10))



first = True
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    root.fill(blue)

    sideLength = 60
    if first == True:
        tiles, vertices, edges = makeMap(50, 100, sideLength)
        first = False
    drawTiles(tiles, sideLength)
    drawNumbers(tiles, sideLength)
    drawVertices(vertices)
    drawEdges(edges)


    pygame.display.flip()
