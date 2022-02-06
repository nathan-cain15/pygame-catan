import math
import pygame
import random
from classes import *


class Game:
    def __init__(self, root, tiles, edges, vertices):
        self.root = root
        self.tiles = tiles
        self.edges = edges
        self.vertices = vertices
        self.notAvalVertices = []
        self.notAvalEdges = []
        self.states = ["starting turns", "regular turn"]
        self.currentState = "starting turns"
        self.substates = ["building", "road"]
        self.currentSubState = "building"

    def placeBuilding(self, player, players, sidelength, mouse, click):
        vertice = self.verticesPressed(mouse, click)
        if vertice != None:
            if (vertice not in self.notAvalVertices) and self.buildingValid(players, vertice, sidelength):
                player.buildings.append(
                    Building(vertice.x, vertice.y, vertice.width, vertice.height, vertice.color, player))
                vertice.color = player.color
                self.notAvalVertices.append(vertice)
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

    def drawTiles(self):
        for tile in self.tiles:
            tile.draw(self.root, tile.color)

    def drawVertices(self):
        for vertice in self.vertices:
            vertice.draw(self.root, vertice.color)

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

    def roadValid(self, player, road):
        for building in player.buildings:
            if ((road.x1 >= building.x - 3 and road.x1 <= building.x) and (
                    road.y1 >= building.y - 3 and road.y1 <= building.y)) or (
                    (road.x2 >= building.x - 3 and road.x2 <= building.x) and (
                    road.y2 >= building.y - 3 and road.y2 <= building.y)):
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
