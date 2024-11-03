import pygame

class Pokemon:
    def __init__(self, name, health, power, moves, x_pos, y_pos):
        print('Player created')
        self.image = pygame.image.load("1.png")
        self.name = name
        self.health = health
        self.power = power
        self.moves = moves
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = pygame.Rect(self.x_pos, self.y_pos)

    def render(self, screen):
        screen.blit(self.image) 

