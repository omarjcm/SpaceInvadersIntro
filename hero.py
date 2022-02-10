from re import X

from pandas import wide_to_long


class Hero:
    def __init__(self, game, x, y):
        self.game = game
        self.x = X
        self.y = y

    def draw(self):
        pygame.draw.rect(self.game.screen, 
                            (210, 250, 251),
                            pygame.Rect(self.x, self.y, 8, 5))

hero = Hero(self, width/2, height-20)
hero.draw()