from pygame.locals import *
from random import randint
import pygame
import time

STEP = 70
MAP_WIDTH = 10 * STEP
MAP_HEIGHT = 10 * STEP


class Apple:

    def __init__(self, x=0, y=0):
        self.x = x * STEP
        self.y = y * STEP

    def draw(self, surface, image):
        surface.blit(image,(self.x, self.y))


class Agent:
    direction = 0

    updateCountMax = 2
    updateCount = 0

    def __init__(self):

       # initial positions
       self.x = 1 * 70
       self.y = 4 * 70

    def update(self):

        self.updateCount += 1
        if self.updateCount > self.updateCountMax:

            # move based on facing direction
            if self.direction == 0:
                self.x += STEP
            if self.direction == 1:
                self.x -= STEP
            if self.direction == 2:
                self.y -= STEP
            if self.direction == 3:
                self.y += STEP

            self.updateCount = 0


    def moveRight(self):
        self.direction = 0

    def moveLeft(self):
        self.direction = 1

    def moveUp(self):
        self.direction = 2

    def moveDown(self):
        self.direction = 3


    def target(self, dx, dy):
        """
        Current movement is based on a 'goal'.
        Need to remove this in place of a path-mapper system.
        + add collision based on walls and/or objects list (yet to do)
        """
        if self.x > dx:
            self.moveLeft()

        if self.x < dx:
            self.moveRight()

        if self.x == dx:
            if self.y < dy:
                self.moveDown()

            if self.y > dy:
                self.moveUp()

    def draw(self, surface, image):
        surface.blit(image,(self.x, self.y))


class Game:
    def isCollision(self, x1, y1, x2, y2, bsize):
        if x1 >= x2 and x1 <= x2 + bsize:
            if y1 >= y2 and y1 <= y2 + bsize:
                return True
        return False

class App:

    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._apple_surf = None
        self.game = Game()
        self.apple = Apple(8,5)
        self.agent = Agent()

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((MAP_WIDTH, MAP_HEIGHT), pygame.HWSURFACE)

        pygame.display.set_caption('Alex')
        self._running = True
        self._image_surf = pygame.image.load("player70.png").convert()
        self._apple_surf = pygame.image.load("block.png").convert()

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        self.agent.target(self.apple.x, self.apple.y)
        self.agent.update()

        # does agent reach goal?
        if self.game.isCollision(self.apple.x,self.apple.y,self.agent.x, self.agent.y,35):
            self.apple.x = randint(0, MAP_WIDTH/70 - 1) * 70
            self.apple.y = randint(0, MAP_HEIGHT/70 - 1) * 70

        pass

    def on_render(self):
        self._display_surf.fill((0,0,0))
        self.apple.draw(self._display_surf, self._apple_surf)
        self.agent.draw(self._display_surf, self._image_surf)
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while( self._running ):
            # hold escape to exit sim
            pygame.event.pump()
            keys = pygame.key.get_pressed()
            if (keys[K_ESCAPE]):
                self._running = False

            # loop game in frame increments
            self.on_loop()
            self.on_render()

            time.sleep (25.0 / 1000.0);
        # cleanup on exit
        self.on_cleanup()

if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
