import math
import pygame
import random

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

class Building(Vertice):
    def __init__(self, x, y, width, height, color, player):
        self.player = player

        Vertice.__init__(self, x, y, width, height, color)

class Road(Edge):
    def __init__(self, x1, y1, x2, y2, color, player):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color
        self.player = player

        Edge.__init__(self, x1, y1, x2, y2, color)


class Button:
    def __init__(self, root, x, y):
        self.root = root
        self.x = x
        self.y = y
        self.width = 0
        self.height = 0

    def draw(self, color1, color2, text, size):
        #pygame.draw.rect(surface, color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont('Comic Sans MS', size)
        textSurface = font.render(text, True, color1, color2)
        textRect = textSurface.get_rect()
        self.width = textRect[2]
        self.height = textRect[3]

        self.root.blit(textSurface, (self.x, self.y))

    def pressed(self, mouse, click):
        if (self.x <= mouse[0] and mouse[0] <= self.x + self.width) and (self.y <= mouse[1] and mouse[1] <= self.y + self.height) and click[0] == True:
            return True
        return False




