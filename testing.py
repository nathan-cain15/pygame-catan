import math
import pygame

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


def drawMap2(x, y, sideLength):
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

    points = getPoints(11, tiles[12][0], tiles[12][1], 41)
    tile = [points[4][0], points[4][1] + sideLength]
    for i in range(3):
        tiles.append(tile)
        points = getPoints(11, tile[0], tile[1], 41)
        tile = points[3]



    for i in tiles:
        drawHexagon(root, grey, 11, i[0], i[1], 41)



def drawMap(x, y, sideLength):
    coords = []
    diagonal = math.sqrt(3) * sideLength

    coords.append((x, y))
    coords.append((x + diagonal, y))
    coords.append((x + (2 * diagonal), y))

    # x = x - (diagonal/2)
    # y = int(y + int(1.5(sideLength)))
    for i in range(5):
        coords.append((x, y))
        x += diagonal

    # coords.append(())
    for i in coords:
        drawHexagon(root, darkGreen, 11, i[0], i[1], 41)


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
    drawMap2(50, 100, 60)

    pygame.display.flip()
