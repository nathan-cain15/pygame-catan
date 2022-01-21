import math
import pygame
import random

class Tile:
    def __init__(self, color, x, y, number):
        self.color = color
        self.x = x
        self.y = y
        self.number = number

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

class Vertice:
    def __init__(self, x, y):
        self.x = x
        self.y = y





