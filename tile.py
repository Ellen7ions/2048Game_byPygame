import random

import pygame
import setting
import events

from pygame.sprite import Sprite

class Tiles(Sprite):
    def __init__(self, number, rect, x, y):
        super().__init__()
        self.number = number
        self.color = self.getColor()
        self.rect = rect
        self.x = x
        self.y = y
        self.image = pygame.image.load('src/' + str(self.number) + '.bmp')


    def getColor(self):
        dic = {
            2 : (255, 215, 0),
            4 : (255, 193, 37),
            8 : (205, 155, 29),
            16 : (255, 127, 80),
            32 : (255, 69, 0),
            64 : (186, 85, 211),
            128 : (139, 90, 43),
            256 : (105, 89, 205),
            512 : (198, 226, 255),
            1024 : (102, 139, 139),
            2048 : (178, 34, 34)
        }
        return dic[self.number]

    def changeRect(self, rect):
        self.rect = rect

    def drawTile(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.image, self.rect)

    def moveXTile(self, settings, p):
        if self.x + p > 0 and self.x + p < 5:
            rect = pygame.Rect(events.getPos(self.x + p, settings), events.getPos(self.y, settings), settings.tileWidth,
                               settings.tileHeight)
            self.rect = rect
            self.x += p

    def moveYTile(self, settings, p):
        if self.y + p > 0 and self.y + p < 5:
            rect = pygame.Rect(events.getPos(self.x, settings), events.getPos(self.y + p, settings), settings.tileWidth,
                               settings.tileHeight)
            self.rect = rect
            self.y += p

    def addTile(self, tile, tiles):
        self.number *= 2
        self.color = self.getColor()
        self.rect = tile.rect
        self.x = tile.x
        self.y = tile.y
        self.image = pygame.image.load('src/' + str(self.number) + '.bmp')
        tiles.remove(tile)

    def update(self, settings, direction, tiles):
        if direction == 'LEFT':
            pd = 0
            for tile in tiles.copy():
                if tile.x == self.x - 1 and tile.y == self.y:
                    pd = 1
                    if tile.number == self.number:
                        self.addTile(tile, tiles)
            if pd == 0:
                self.moveXTile(settings, -1)

        elif direction == 'RIGHT':
            pd = 0
            for tile in tiles.copy():
                if tile.x == self.x + 1 and tile.y == self.y:
                    pd = 1
                    if tile.number == self.number:
                        self.addTile(tile, tiles)
            if pd == 0:
                self.moveXTile(settings, 1)

        elif direction == 'UP':
            pd = 0
            for tile in tiles.copy():
                if tile.x == self.x and tile.y == self.y - 1:
                    pd = 1
                    if tile.number == self.number:
                        self.addTile(tile, tiles)
            if pd == 0:
                self.moveYTile(settings, -1)

        elif direction == 'DOWN':
            pd = 0
            for tile in tiles.copy():
                if tile.x == self.x and tile.y == self.y + 1:
                    pd = 1
                    if tile.number == self.number:
                        self.addTile(tile, tiles)
            if pd == 0:
                self.moveYTile(settings, 1)