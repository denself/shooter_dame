import pygame
import settings as s

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
        pygame.display.set_caption("Caligo")

        # self.timedEvent = TimedEvent(168000,self,"music_loop")

        # Loop until the user clicks the close button.
        self.done = False

        # Used to manage how fast the screen updates
        self.clock = pygame.time.Clock()

    def main_loop(self):
        self.initialize()
        while not self.done:

            self.update()
            self.draw()

            # Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

            # Limit to 60 frames per second
            self.clock.tick(60)

        pygame.quit()

    def initialize(self):
        pass

    def draw(self):
        pass
        # self.current_level.draw(self.screen)
        # self.draw_debug_rects()

    def update(self):
        pass
        # self.timedEvent.update()
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                self.done = True  # Flag that we are done so we exit this loop

            # self.current_level.inputProcessor.ProcessEvent(event)


if __name__ == "__main__":
    g_game = GameApplication()
    g_game.main_loop()