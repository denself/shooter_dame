import pygame

from managers import InputManager
from models.entities import TestButton
from models.level import MenuLevel
from resources import ResourceManager
import settings as s
from utils import singleton


@singleton
class GameApplication:
    def __init__(self, width=s.SCREEN_WIDTH, height=s.SCREEN_HEIGHT):
        pygame.init()

        # Set the height and width of the screen
        self.screen_size = [width, height]
        # pygame.display.set_icon("")
        # self.screen = pygame.display.set_mode(self.screen_size)

        # flags = pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF
        flags = pygame.HWSURFACE | pygame.DOUBLEBUF
        self.screen = pygame.display.set_mode(self.screen_size, flags)
        pygame.display.set_caption("Shooter Dame")

        # self.timedEvent = TimedEvent(168000,self,"music_loop")

        # Loop until the user clicks the close button.
        self.done = False

        # Used to manage how fast the screen updates
        self.clock = pygame.time.Clock()

        # Levels
        self.levels = {}
        self.current_level = None
        self.input_manager = None

    def get_level(self):
        return self.levels.get(self.current_level)

    def main_loop(self):
        self.initialize()
        while not self.done:

            self.update()
            self.screen.fill((0, 0, 0))
            self.draw()

            # Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

            ResourceManager().free_unused_resources()
            # Limit to 60 frames per second
            self.clock.tick(60)

        pygame.quit()

    def initialize(self):
        self.input_manager = InputManager()
        menu = MenuLevel()
        menu.entities.append(TestButton())
        self.levels['menu'] = menu
        self.current_level = 'menu'
        pass

    def draw(self):
        self.get_level().draw(self.screen)
        # self.current_level.draw(self.screen)

    def update(self):
        # self.timedEvent.update()
        self.input_manager.update()
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                self.done = True  # Flag that we are done so we exit this loop

        self.get_level().update()


if __name__ == "__main__":
    g_game = GameApplication()
    g_game.main_loop()
