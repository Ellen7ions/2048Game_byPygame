import pygame

class Settings():
    def __init__(self):
        self.screenWidth = 500
        self.screenHeight = 500
        self.tileWidth = (self.screenWidth - 100) / 4
        self.tileHeight = (self.screenHeight - 100) / 4

        self.backgroundColor = (255, 228, 225)
        # self.background = pygame.image.load('')
