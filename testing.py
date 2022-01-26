import math
import random

import pygame

from classes import Edge
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
black = (0, 0, 0)


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


def makeTiles(x, y, sideLength):
    tiles = []
    tile = [x, y]
    tilePoints = []
    num = 0
    for i in range(5):
        tiles.append(tile)
        points = getPoints(11, tile[0], tile[1], sideLength)
        tilePoints.append(points)
        tile = points[3]
        num += 1

    points = getPoints(11, tiles[0][0], tiles[0][1], sideLength)
    tile = [points[4][0], points[4][1] + sideLength]
    del tiles[0:2]
    del tilePoints[0:2]

    for i in range(5):
        tiles.append(tile)
        points = getPoints(11, tile[0], tile[1], sideLength)
        tilePoints.append(points)
        tile = points[3]
        num += 1

    points = getPoints(11, tiles[3][0], tiles[3][1], sideLength)
    tile = [points[4][0], points[4][1] + sideLength]
    tiles.remove(tiles[3])
    tilePoints.remove(tilePoints[3])

    for i in range(5):
        tiles.append(tile)
        points = getPoints(11, tile[0], tile[1], sideLength)
        tilePoints.append(points)
        tile = points[3]

    points = getPoints(11, tiles[7][0], tiles[7][1], sideLength)
    tile = [points[4][0], points[4][1] + sideLength]

    for i in range(4):
        tiles.append(tile)
        points = getPoints(11, tile[0], tile[1], sideLength)
        tilePoints.append(points)
        tile = points[3]

    points = getPoints(11, tiles[12][0], tiles[12][1], sideLength)
    tile = [points[4][0], points[4][1] + sideLength]
    for i in range(3):
        tiles.append(tile)
        points = getPoints(11, tile[0], tile[1], sideLength)
        tilePoints.append(points)
        tile = points[3]

    colors = randomColors(4, 4, 3, 4, 3, 1)
    tilesList = []

    number = 0
    for tile in tiles:
        tilesList.append(Tile(colors[number], tile[0], tile[1], 1, tilePoints[number]))
        number += 1
    tilesList = generateNumbers(tilesList)

    return tilesList

def makeVertices(tiles, width, height):
    points = []
    for tile in tiles:
        for point in tile.points:
            if point not in points:
                points.append(point)
    for pnt in points:
        for tile in tiles:
            for point in tile.points:
                if point != pnt and (point[0] >= pnt[0] - 5 and point[0] <= pnt[0] + 5) and (point[1] >= pnt[1] - 5 and point[1] <= pnt[1] + 5):
                    tile.points[tile.points.index(point)] = pnt
    vertices = []
    for tile in tiles:
        for point in tile.points:
            if point not in vertices:
                vertices.append(point)
    verticeList = []
    for vertice in vertices:
        verticeList.append(Vertice(vertice[0], vertice[1], width, height))
    return verticeList

def makeEdges(tiles):
    edges = []
    for tile in tiles:
        if [tile.points[5], tile.points[0]] and [tile.points[0], tile.points[5]] not in edges:
            edges.append([tile.points[5], tile.points[0]])
        num = 0
        for i in range(5):
            if [tile.points[i], tile.points[i+1]] and [tile.points[i+1], tile.points[i]] not in edges:
                edges.append([tile.points[i], tile.points[i+1]])
    edgeList = []
    for edge in edges:
        edgeList.append(Edge(edge[0][0], edge[0][1], edge[1][0], edge[1][1]))
    return edgeList


def drawTiles(tiles, sideLength):
    for i in tiles:
        i.draw(root, i.color)

def drawVertices(vertices):
    for i in vertices:
        i.draw(root, white)

def drawEdges(edges):
    for edge in edges:
            if edge.x1 - 1 == edge.x2:
                edge.x1 = edge.x2
    for edge in edges:
        if edge.x1 == edge.x2:
            pygame.draw.polygon(root, white, ((edge.x1 - 2, edge.y1),  (edge.x2 - 2, edge.y2), (edge.x2 + 2, edge.y2), (edge.x1 + 2, edge.y1)))
        else:
            pygame.draw.polygon(root, white, ((edge.x1 - 3, edge.y1),  (edge.x2 - 3, edge.y2), (edge.x2 + 3, edge.y2), (edge.x1 + 3, edge.y1)))

def drawNumbers(tiles, sidelength):
    diagonal = math.sqrt(3) * sidelength
    myfont = pygame.font.SysFont('Comic Sans MS', 20)
    for tile in tiles:
        if tile.number == 1:
            continue
        num = str(tile.number)
        textsurface = myfont.render(num, False, (0, 0, 0))
        root.blit(textsurface, (tile.x + (diagonal/2 - 5), tile.y - sidelength + 10))

def verticesPressed(vertices, mouse, click):
    for i in vertices:
        clicked = i.pressed(mouse, click)
        if clicked:
            print("yes")

def edgesPressed(edges, mouse, click):
    for i in edges:
        clicked = i.pressed(mouse, click)
        if clicked:
            print("yes")

def tilePressed(tiles, mouse, click):
    centers = []
    for i in tiles:
        centers.append(i.getCenter(60))
    if click[0] == True:
        shortestDistance = 1000
        for center in centers:
            distanceX = abs(center[0] - mouse[0])
            distanceY = abs(center[1] - mouse[1])
            distance = math.sqrt(distanceX**2 + distanceY**2)
            if distance < shortestDistance:
                shortestDistance = distance
                tile = tiles[centers.index(center)]
        print(tile.color)





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
        tiles = makeTiles(60, 100, sideLength)
        vertices = makeVertices(tiles, 10, 10)
        edges = makeEdges(tiles)
        first = False

    drawTiles(tiles, sideLength)
    drawNumbers(tiles, sideLength)
    #drawVertices(vertices)
    drawEdges(edges)

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    #edgesPressed(edges, mouse, click)
    tilePressed(tiles, mouse, click)
    pygame.display.flip()
