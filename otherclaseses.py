import math
import pygame
import random
from game import *

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
        self.resources = [0, 0, 0, 0, 0]


class Building(Vertice):
    def __init__(self, x, y, width, height, color, player):
        self.player = player

        Vertice.__init__(self, x, y, width, height, color)

class Road(Edge):
    def __init__(self, x1, y1, x2, y2, color, player):
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

class PlayerDisplay:
    def __init__(self, root, x, y, player):
        self.player = player
        self.root = root
        self.x = x
        self.y = y
        self.player = player

    def draw(self, width, height, textColor, boxColor, spacing, ratio, fontSize):
        font = pygame.font.SysFont('Comic Sans MS', fontSize)

        materials = [self.player.resources[0], self.player.resources[1], self.player.resources[2], self.player.resources[3], self.player.resources[4]]
        words = ["wood", "brick", "sheep", "wheat", "ore"]
        space = 0

        for i in range(5):
            pygame.draw.rect(self.root, self.player.color, (self.x + space, self.y, width, height))
            pygame.draw.rect(self.root, boxColor, (self.x + space + int((width - (ratio * width)) / 2), self.y + int((height - (ratio * height)) / 2), int(width * ratio), int(height * ratio)))

            number = font.render(str(materials[i]), False, textColor)
            self.root.blit(number, (self.x + space + (width / 3), self.y))

            text = font.render(words[i], False, textColor)
            rect = text.get_rect()
            self.root.blit(text, (int(self.x + space + (width - rect[2]) / 2), self.y + height - 5))

            space += spacing

class Dice(Button):
    def __init__(self, root, x, y):
        self.root = root
        self.x = x
        self.y = y
        self.die1 = 0
        self.die2 = 0

    def drawDice(self, x, y, width, height, color1, color2, size, space, ratio):
        font = pygame.font.SysFont('Comic Sans MS', size)
        textSurface = font.render(str(self.die1), False, color1)

        pygame.draw.rect(self.root, color1, (x, y, width, height))
        pygame.draw.rect(self.root, color2, (
        x + int((width - (ratio * width)) / 2), y + int((height - (ratio * height)) / 2),
        int(width * ratio), int(height * ratio)))

        self.root.blit(textSurface, (x + (width / 3), y))

        textSurface = font.render(str(self.die2), False, color1)

        pygame.draw.rect(self.root, color1, (x + space, y, width, height))
        pygame.draw.rect(self.root, color2, (
            x + space + int((width - (ratio * width)) / 2), y + int((height - (ratio * height)) / 2),
            int(width * ratio), int(height * ratio)))

        self.root.blit(textSurface, (x + space + (width / 3), y))

    def roll(self):
        self.die1 = random.choice(range(1, 6))
        self.die2 = random.choice(range(1, 6))