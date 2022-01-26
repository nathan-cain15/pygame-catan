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
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, surface, color):
        pygame.draw.rect(surface, color, (self.x - (self.width / 2), self.y - (self.height / 2), self.width, self.height))

    def pressed(self, mouse, click):
        if (self.x - (self.width / 2) <= mouse[0] and mouse[0] <= self.x - (self.width / 2) + self.width) and (self.y - (self.height / 2) <= mouse[1] and mouse[1] <= self.y - (self.height / 2) + self.height) and click[0] == True:
            return True


class Edge:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
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








