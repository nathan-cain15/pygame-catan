import math
import pygame
import random
from otherclaseses import *



class Game:
    def __init__(self, root, tiles, edges, vertices):
        self.root = root
        self.tiles = tiles
        self.edges = edges
        self.vertices = vertices
        self.notAvalVertices = []
        self.notAvalEdges = []
        self.currentState = "starting turns"
        self.currentSubState = "building"
        self.robber = None

    def placeBuilding(self, player, players, sideLength, mouse, click):
        vertice = self.verticesPressed(mouse, click)
        if vertice != None:
            if (vertice not in self.notAvalVertices) and self.buildingValid(players, vertice, sideLength):
                building = Building(vertice.x, vertice.y, vertice.width, vertice.height, vertice.color, player)
                player.buildings.append(building)
                vertice.color = player.color
                self.notAvalVertices.append(vertice)

                player.victoryPoints += 1
                return True
        else:
            return False

    def placeRoad(self, player, mouse, click):
        edge = self.edgesPressed(mouse, click)
        if edge != None:
            if edge not in self.notAvalEdges and self.roadValid(player, edge):
                player.roads.append(Road(edge.x1, edge.y1, edge.x2, edge.y2, edge.color, player))
                edge.color = player.color
                self.notAvalEdges.append(edge)
                return True
        else:
            return False

    def buildBuilding(self, player, players, sideLength, mouse, click):
        vertice = self.verticesPressed(mouse, click)
        if vertice != None:
            if (vertice not in self.notAvalVertices) and self.buildingValid(players, vertice, sideLength) and player.resources[0] >= 1 and player.resources[1] >= 1 and player.resources[2] >= 1 and player.resources[3] >= 1:
                building = Building(vertice.x, vertice.y, vertice.width, vertice.height, vertice.color, player)
                player.buildings.append(building)
                vertice.color = player.color
                self.notAvalVertices.append(vertice)

                player.victoryPoints += 1
                for i in range(4):
                    player.resources[i] -= 1
                return True
        else:
            return False

    def buildRoad(self, player, mouse, click):
        edge = self.edgesPressed(mouse, click)
        if edge != None:
            if edge not in self.notAvalEdges and self.roadValid(player, edge) and player.resources[0] >= 1 and player.resources[1] >= 1:
                player.roads.append(Road(edge.x1, edge.y1, edge.x2, edge.y2, edge.color, player))
                edge.color = player.color
                self.notAvalEdges.append(edge)

                player.resources[0] -= 1
                player.resources[1] -= 1
                return True
        else:
            return False

    def buildCity(self, player, mouse, click):
        building = self.verticesPressed(mouse, click)

        if building != None:# and player.resources[3] >= 2 and player.resources[4] >= 3:
            for settlement in player.buildings:
                if building.x == settlement.x and building.y == settlement.y:
                    player.cities.append(settlement)
                    player.buildings.remove(settlement)
                    building.isCity = True
                    return True
        else:
            return False

    def drawTiles(self):
        for tile in self.tiles:
            tile.draw(self.root, tile.color)

    def drawVertices(self):
        for vertice in self.vertices:
            vertice.draw(self.root, vertice.color)
            if vertice.isCity:
                pygame.draw.circle(self.root, (0, 0, 0), (vertice.x, vertice.y), 2)

    def drawEdges(self):
        for edge in self.edges:
            if edge.x1 - 1 == edge.x2:
                edge.x1 = edge.x2
        for edge in self.edges:
            if edge.x1 == edge.x2:
                pygame.draw.polygon(self.root, edge.color, (
                    (edge.x1 - 2, edge.y1), (edge.x2 - 2, edge.y2), (edge.x2 + 2, edge.y2), (edge.x1 + 2, edge.y1)))
            else:
                pygame.draw.polygon(self.root, edge.color, (
                    (edge.x1 - 3, edge.y1), (edge.x2 - 3, edge.y2), (edge.x2 + 3, edge.y2), (edge.x1 + 3, edge.y1)))

    def verticesPressed(self, mouse, click):
        for vert in self.vertices:
            clicked = vert.pressed(mouse, click)
            if clicked:
                return vert

    def edgesPressed(self, mouse, click):
        for edge in self.edges:
            clicked = edge.pressed(mouse, click)
            if clicked:
                return edge

    def tilePressed(self, mouse, click):
        centers = []
        for tile in self.tiles:
            centers.append(tile.getCenter(60))
        if click[0] == True:
            shortestDistance = 1000
            for center in centers:
                distanceX = abs(center[0] - mouse[0])
                distanceY = abs(center[1] - mouse[1])
                distance = math.sqrt(distanceX ** 2 + distanceY ** 2)
                if distance < shortestDistance:
                    shortestDistance = distance
                    pressedTile = self.tiles[centers.index(center)]
            return pressedTile

    def roadValid(self, player, road):
        for building in player.buildings:
            if ((building.x - 3 <= road.x1 <= building.x) and (
                    building.y - 3 <= road.y1 <= building.y)) or (
                    (building.x - 3 <= road.x2 <= building.x) and (
                    building.y - 3 <= road.y2 <= building.y)):
                return True
        for playerRoad in player.roads:
            if ((playerRoad.x1 - 5 <= road.x1 <= playerRoad.x1 + 5) and (
                    playerRoad.y1 - 5 <= road.y1 <= playerRoad.y1 + 5)) or (
                    (playerRoad.x2 - 5 <= road.x1 <= playerRoad.x2 + 5) and (
                    playerRoad.y2 - 5 <= road.y1 <= playerRoad.y2 + 5)) or (
                    (playerRoad.x1 - 5 <= road.x2 <= playerRoad.x1 + 5) and (
                    playerRoad.y1 - 5 <= road.y2 <= playerRoad.y1 + 5)) or (
                    (playerRoad.x2 - 5 <= road.x2 <= playerRoad.x2 + 5) and (
                    playerRoad.y2 - 5 <= road.y2 <= playerRoad.y2 + 5)):
                return True

        return False

    def buildingValid(self, players, building, sidelength):
        for player in players:
            for build in player.buildings:
                if (building.x >= build.x - (sidelength + (sidelength/6))) and (
                        building.x <= build.x + (sidelength + (sidelength/6))) and (
                        building.y >= build.y - (sidelength + (sidelength/6))) and (
                        building.y <= build.y + (sidelength + (sidelength/6))):
                    return False
        return True

    def getStartingResources(self, vertice, player):
        dictionary = {
            (55, 75, 30): 0,
            (156, 67, 0): 1,
            (81, 125, 25): 2,
            (240, 173, 0): 3,
            (123, 111, 131): 4,
        }
        for tile in self.tiles:
            for point in tile.points:
                if (vertice.x >= point[0] -3 and vertice.x <= point[0] + 3) and (vertice.y >= point[1] - 3 and vertice.y <= point[1] + 3):

                    if tile.color != (243, 192, 114):

                        player.resources[dictionary[tile.color]] += 1

    def giveResources(self, dice, players):
        num = dice.die1 + dice.die2
        tilesWithNum = []

        dictionary = {
            (55, 75, 30): 0,
            (156, 67, 0): 1,
            (81, 125, 25): 2,
            (240, 173, 0): 3,
            (123, 111, 131): 4,
        }
        for tile in self.tiles:
            if tile.number == num and self.robber.tile != tile:
                tilesWithNum.append(tile)

        for tile in tilesWithNum:
            for point in tile.points:
                for player in players:
                    for building in player.buildings:
                        if (building.x >= point[0] -3 and building.x <= point[0] + 3) and (building.y >= point[1] - 3 and building.y <= point[1] + 3):
                            player.resources[dictionary[tile.color]] += 1

                    for city in player.cities:
                        if (city.x >= point[0] -3 and city.x <= point[0] + 3) and (city.y >= point[1] - 3 and city.y <= point[1] + 3):
                            player.resources[dictionary[tile.color]] += 2

    def setRobber(self):
        for tile in self.tiles:
            if tile.color == (243, 192, 114):
                self.robber = Robber(tile, self.root)

    def checkResources(self, players):
        for player in players:
            resourceAmount = 0
            for resource in player.resources:
                resourceAmount += resource
            if resourceAmount > 7:
                halfOfResources = int(resourceAmount/2)

                while halfOfResources != 0:

                    while True:
                        randomNum = random.choice(range(0, 5))
                        if player.resources[randomNum] != 0:
                            break

                    player.resources[randomNum] -= 1
                    halfOfResources -= 1

    def displayPressed(self, mouse, click, displays, number):
        for display in displays:
            if displays[number] == display:
                continue
            pressedResource = display.pressed(mouse, click)
            if pressedResource != None:
                return display, pressedResource

