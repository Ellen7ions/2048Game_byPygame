import pygame, sys, random
import setting

from tile import Tiles
from setting import Settings

def getPos(x, settings):
    return 20 + (x - 1) * (settings.tileWidth + 20)

def spawnTile(tiles, rect, x, y, number = 2):
    tile = Tiles(number, rect, x, y)
    tiles.add(tile)
    return tile

def checkAvailableSpaw(rect, tiles):
    for tile in tiles:
        if rect.centerx == tile.rect.centerx and rect.centery == tile.rect.centery:
            return False
    return True

def spawnRandom(settings, tiles):
    x = random.randint(1, 4)
    y = random.randint(1, 4)
    rect = pygame.Rect(getPos(x, settings), getPos(y, settings), settings.tileWidth, settings.tileHeight)
    while checkAvailableSpaw(rect, tiles) == False:
        x = random.randint(1, 4)
        y = random.randint(1, 4)
        rect = pygame.Rect(getPos(x, settings), getPos(y, settings), settings.tileWidth, settings.tileHeight)
    spawnTile(tiles, rect, x, y)

def spawnFirstTiles(tiles, settings):
    cntTiles = random.randint(2, 3)
    # cntTiles = 16
    while cntTiles > 0:
        x = random.randint(1, 4)
        y = random.randint(1, 4)
        rect = pygame.Rect(getPos(x, settings), getPos(y, settings), settings.tileWidth, settings.tileHeight)
        # print(str(cntTiles) + ":" + str(rect.centerx) + " " + str(rect.centery))
        if checkAvailableSpaw(rect, tiles):
            newTile = spawnTile(tiles, rect, x , y)
            cntTiles -= 1
        else:
            continue


def screenInit(settings):
    pygame.init()
    screen = pygame.display.set_mode((settings.screenWidth, settings.screenHeight))
    pygame.display.set_caption('2048')
    screen.fill(settings.backgroundColor)
    return screen

def eventResponse(settings, tiles):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                for i in range(4):
                    tiles.update(settings, 'LEFT', tiles)
                # for tile in tiles:
                #     print(tile.x, tile.y)
                # input()
            elif event.key == pygame.K_RIGHT:
                for i in range(4):
                    tiles.update(settings, 'RIGHT', tiles)
            elif event.key == pygame.K_UP:
                for i in range(4):
                    tiles.update(settings, 'UP', tiles)
            elif event.key == pygame.K_DOWN:
                for i in range(4):
                    tiles.update(settings, 'DOWN', tiles)
            spawnRandom(settings, tiles)

def freshScreen(settings, screen, tiles):
    screen.fill(settings.backgroundColor)
    for tile in tiles:
        tile.drawTile(screen)
    pygame.display.flip()