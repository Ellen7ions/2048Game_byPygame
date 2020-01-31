import pygame, sys
import events

from pygame.sprite import Group
from setting import Settings

def main():
    settings = Settings()
    screen = events.screenInit(settings)
    tiles = Group()
    events.spawnFirstTiles(tiles, settings)
    while True:
        events.eventResponse(settings, tiles)

        events.freshScreen(settings, screen, tiles)

if __name__ == '__main__':
    main()