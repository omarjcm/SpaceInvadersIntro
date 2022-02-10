import pygame
from alien import Alien
from generator import Generator
from hero import Hero

'''
Codigo fuente: https://github.com/janjilecek/pygame-invaders/blob/master/main.py
'''

class Game:
    screen = None
    aliens = []

    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode( (width, height) )
        self.clock = pygame.time.Clock()
        done = False

        hero = Hero(self, width/2, height-20)
        generator = Generator(self)

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                
            pygame.display.flip()
            self.clock.tick(60)
            self.screen.fill((0, 0, 0))

            for alien in self.aliens:
                alien.draw()

            hero.draw()

if __name__ == '__main__':
    game = Game(600, 400)