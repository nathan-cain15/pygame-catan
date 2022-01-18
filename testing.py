import math
import pygame
import random

pygame.init()
root = pygame.display.set_mode((900, 600))

lightGreen = (81, 125, 25)
darkGreen = (55, 75, 30)
blue = (79, 166, 235)
yellow = (240, 173, 0)
red = (156, 67, 0)
grey = (123, 111, 131)
tan = (243, 192, 114)

class Tile:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y

    def draw(self, surface, color, tiltAngle, x, y, radius):
        pts = []
        for i in range(6):
            x = x + radius * math.cos(tiltAngle + math.pi * 2 * i / 6)
            y = y + radius * math.sin(tiltAngle + math.pi * 2 * i / 6)
            pts.append([int(x), int(y)])
        pygame.draw.polygon(surface, color, pts)

    def getThePoints(self, surface, color, tiltAngle, x, y, radius):
        pts = []
        for i in range(6):
            x = x + radius * math.cos(tiltAngle + math.pi * 2 * i / 6)
            y = y + radius * math.sin(tiltAngle + math.pi * 2 * i / 6)
            pts.append([int(x), int(y)])
        return pts


def drawHexagon(surface, color, tiltAngle, x, y, radius):
    pts = []
    for i in range(6):
        x = x + radius * math.cos(tiltAngle + math.pi * 2 * i / 6)
        y = y + radius * math.sin(tiltAngle + math.pi * 2 * i / 6)
        pts.append([int(x), int(y)])
    pygame.draw.polygon(surface, color, pts)

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


def makeMap(x, y, sideLength):
    tiles = []
    tile = [x, y]
    for i in range(5):
        tiles.append(tile)
        points = getPoints(11, tile[0], tile[1], sideLength)
        tile = points[3]

    points = getPoints(11, tiles[0][0], tiles[0][1], sideLength)
    tile = [points[4][0], points[4][1] + sideLength]
    tiles.remove(tiles[0])
    tiles.remove(tiles[0])

    for i in range(5):
        tiles.append(tile)
        points = getPoints(11, tile[0], tile[1], sideLength)
        tile = points[3]

    points = getPoints(11, tiles[3][0], tiles[3][1], sideLength)
    tile = [points[4][0], points[4][1] + sideLength]
    tiles.remove(tiles[3])

    for i in range(5):
        tiles.append(tile)
        points = getPoints(11, tile[0], tile[1], sideLength)
        tile = points[3]

    points = getPoints(11, tiles[7][0], tiles[7][1], sideLength)
    tile = [points[4][0], points[4][1] + sideLength]
    for i in range(4):
        tiles.append(tile)
        points = getPoints(11, tile[0], tile[1], sideLength)
        tile = points[3]

    points = getPoints(11, tiles[12][0], tiles[12][1], sideLength)
    tile = [points[4][0], points[4][1] + sideLength]
    for i in range(3):
        tiles.append(tile)
        points = getPoints(11, tile[0], tile[1], sideLength)
        tile = points[3]

    colors = randomColors(4, 4, 3, 4, 4, 1)
    tilesList = []
    number = 0
    for tile in tiles:
        #drawHexagon(root, colors[random.randint(0, 5)], 11, tile[0], tile[1], sideLength)
        tilesList.append(Tile(colors[number], tile[0], tile[1]))
        number += 1
    return tilesList

def drawMap(tiles, sideLength):
    for i in tiles:
        i.draw(root, i.color, 11, i.x, i.y, sideLength)

first = True
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    root.fill(blue)

    # run = False
    # drawMap(300, 200, 41)
    #hex = drawHexagon(root, grey, 11, 300, 200, 41)
    #print(hex)
    #hex2 = drawHexagon(root, darkGreen, 11, 371, 200, 41)
    #print(hex2)
    if first == True:
        map = makeMap(50, 100, 60)
        first = False
    drawMap(map, 60)

    pygame.display.flip()
