import math
import random
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
white = (249, 238, 225)
black = (0, 0, 0)
playerRed = (196, 34, 23)
playerBlue = (1, 102, 145)
playerBrown = (161, 106, 92)
playerOrange = (236, 102, 7)

class Tile:
    def __init__(self, color, x, y, number, points):
        self.color = color
        self.x = x
        self.y = y
        self.number = number
        self.points = points

    def draw(self, surface, color):
        pts = []
        for i in self.points:
            pts.append(i)

        pygame.draw.polygon(surface, color, pts)

    def getThePoints(self, surface, color, tiltAngle, x, y, radius):
        pts = []
        for i in range(6):
            x = x + radius * math.cos(tiltAngle + math.pi * 2 * i / 6)
            y = y + radius * math.sin(tiltAngle + math.pi * 2 * i / 6)
            pts.append([int(x), int(y)])
        return pts
    def getCenter(self, sidelength):
        pointX = self.points[1][0]
        pointY = self.points[0][1] + int(sidelength/2)
        return [pointX, pointY]


class Vertice:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, surface, color):
        pygame.draw.rect(surface, color, (self.x - (self.width / 2), self.y - (self.height / 2), self.width, self.height))

    def pressed(self, mouse, click):
        if (self.x - (self.width / 2) <= mouse[0] and mouse[0] <= self.x - (self.width / 2) + self.width) and (self.y - (self.height / 2) <= mouse[1] and mouse[1] <= self.y - (self.height / 2) + self.height) and click[0] == True:
            return True
        return False

class Edge:
    def __init__(self, x1, y1, x2, y2, color):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color

    def pressed(self, mouse, click):
        if self.x1 <= self.x2:
            x1 = self.x1
            x2 = self.x2
        else:
            x1 = self.x2
            x2 = self.x1
        if self.y1 <= self.y2:
            y1 = self.y1
            y2 = self.y2
        else:
            y1 = self.y2
            y2 = self.y1
        if (x1-3 <= mouse[0] and mouse[0] <= x2+3 ) and (y1 <= mouse[1] and mouse[1] <= y2) and click[0] == True:
            return True

class Player:
    def __init__(self, color):
        self.color = color
        self.victoryPoints = 0
        self.roads = []
        self.buildings = []

class Building:
    def __init__(self, tile, player):
        self.tile = tile
        self.player = player

class Road:
    def __init__(self, edge, player):
        self.edge = edge
        self.player = player

class Game:
    def __init__(self, tiles, edges, vertices):
        self.tiles = tiles
        self.edges = edges
        self.vertices = vertices
        self.notAvalVertices = []
        self.notAvalEdges = []
        self.mouse = mouse
        self.click = click
        self.states = ["starting turns", "regular turn"]
        self.currentState = "starting turns"
        self.substates = ["building", "road"]
        self.currentSubState = "building"

    def placeBuilding(self, player, mouse, click):
        vertice = verticesPressed(self.vertices, mouse, click)
        if vertice != None:
            if vertice not in self.notAvalVertices:
                player.buildings.append(Building(vertice, player))
                vertice.color = player.color
                self.notAvalVertices.append(vertice)
                return True
        else:
            return False

    def placeRoad(self, player, mouse, click):
        edge = edgesPressed(self.edges, mouse, click)
        if edge != None:
            if edge not in self.notAvalEdges:
                player.roads.append(Road(edge, player))
                edge.color = player.color
                self.notAvalEdges.append(edge)
                return True
        else:
            return False

    def drawTiles(self):
        for tile in self.tiles:
            tile.draw(root, tile.color)

    def drawVertices(self):
        for vertice in self.vertices:
            vertice.draw(root, vertice.color)

    def drawEdges(self):
        for edge in self.edges:
            if edge.x1 - 1 == edge.x2:
                edge.x1 = edge.x2
        for edge in edges:
            if edge.x1 == edge.x2:
                pygame.draw.polygon(root, edge.color, (
                (edge.x1 - 2, edge.y1), (edge.x2 - 2, edge.y2), (edge.x2 + 2, edge.y2), (edge.x1 + 2, edge.y1)))
            else:
                pygame.draw.polygon(root, edge.color, (
                (edge.x1 - 3, edge.y1), (edge.x2 - 3, edge.y2), (edge.x2 + 3, edge.y2), (edge.x1 + 3, edge.y1)))

    def roadValid(self, player, road):

class Button:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 0
        self.height = 0

    def draw(self, surface, color, text, size):
        #pygame.draw.rect(surface, color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont('Comic Sans MS', size)
        textSurface = font.render(text, True, black, white)
        textRect = textSurface.get_rect()
        self.width = textRect[2]
        self.height = textRect[3]

        root.blit(textSurface, (self.x, self.y))

    def pressed(self, mouse, click):
        if (self.x <= mouse[0] and mouse[0] <= self.x + self.width) and (self.y <= mouse[1] and mouse[1] <= self.y + self.height) and click[0] == True:
            return True
        return False



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
        verticeList.append(Vertice(vertice[0], vertice[1], width, height, white))
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
        edgeList.append(Edge(edge[0][0], edge[0][1], edge[1][0], edge[1][1], white))
    return edgeList

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
    for vert in vertices:
        clicked = vert.pressed(mouse, click)
        if clicked:
            return vert


def edgesPressed(edges, mouse, click):
    for edge in edges:
        clicked = edge.pressed(mouse, click)
        if clicked:
            return edge

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
        return tile


sideLength = 60
first = True
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    root.fill(blue)
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()


    if first == True:
        tiles = makeTiles(-80, 130, sideLength)
        vertices = makeVertices(tiles, 10, 10)
        edges = makeEdges(tiles)
        game = Game(tiles, edges, vertices)

        player1 = Player(playerBlue)
        player2 = Player(playerBrown)
        player3 = Player(playerOrange)
        player4 = Player(playerRed)
        players = [player1, player2, player3, player4]

        buildButton = Button(600, 100)
        roadButton = Button(600, 200)


        number = 0
        buildPressed = False
        roadPressed = False
        first = False

    game.drawTiles()
    drawNumbers(tiles, sideLength)
    game.drawEdges()
    game.drawVertices()

    buildButton.draw(root, white, "build settlement", 20)
    roadButton.draw(root, white, "build road", 20)

    if buildPressed == False:
        buildPressed = buildButton.pressed(mouse, click)
    if roadPressed == False:
        roadPressed = roadButton.pressed(mouse, click)

    if game.currentState == "starting turns":
        if game.currentSubState == "building" and buildPressed == True:
            ran = game.placeBuilding(players[number], mouse, click)
            if ran:
                game.currentSubState = "road"
                buildPressed = False
        elif game.currentSubState == "road" and roadPressed == True:
            ran = game.placeRoad(players[number], mouse, click)
            if ran:
                game.currentSubState = "building"
                roadPressed = False
                if number == 3:
                    number = 0
                else:
                    number += 1




    pygame.display.flip()
