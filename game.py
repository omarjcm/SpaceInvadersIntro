import pygame
from alien import Alien
from generator import Generator
from hero import Hero
from rocket import Rocket

'''
Codigo fuente: https://github.com/janjilecek/pygame-invaders/blob/master/main.py
'''

class Game:
    screen = None
    aliens = []
    rockets = []
    lost = False

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
            if len(self.aliens) == 0:
                self.displayText('VICTORIA ALCANZADA')

            pressed = pygame.key.get_pressed()

            if pressed[pygame.K_LEFT]:
                # Movimiento a la izquierda
                hero.x -= 2 if hero.x > 20 else 0
            elif pressed[pygame.K_RIGHT]:
                # Movimiento a la derecha
                hero.x += 2 if hero.x < width - 20 else 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.rockets.append( Rocket(self, hero.x, hero.y) )
                
            pygame.display.flip()
            self.clock.tick(60)
            self.screen.fill((0, 0, 0))

            for alien in self.aliens:
                alien.draw()
                alien.checkCollision(self)

                if (alien.y > self.height):
                    self.lost = True
                    self.displayText('PERDISTE!')

            for rocket in self.rockets:
                rocket.draw()

            if not self.lost:
                hero.draw()

    
    def displayText(self, text):
        pygame.font.init()
        font = pygame.font.SysFont('Arial', 50)
        textsurface = font.render(text, False, (44, 0, 62))
        self.screen.blit(textsurface, (110, 160))

if __name__ == '__main__':
    game = Game(600, 400)