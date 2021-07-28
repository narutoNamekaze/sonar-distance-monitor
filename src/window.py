import pygame
import sys

import constants

class Window:
    def __init__(self) -> None:
        pygame.init()
        self.running = True
        self.width, self.height = constants.SCREEN_SIZE
        self.screen = pygame.display.set_mode(constants.SCREEN_SIZE)
        self.font = pygame.font.SysFont(None, constants.FONT_SIZE)

        self._text = None
        self._text_image = None

        self._bg = pygame.image.load("background.png")
    
    @property
    def text(self):
        return self._text
    
    @text.setter
    def text(self, value):
        self._text = value
        self._text_image = self.font.render(value, True, constants.COLOR_FOREGROUND)
        self.draw()
        pygame.display.flip()

    def event(self, event):
        if event.type == pygame.QUIT:
            self._exit()
        self.draw()
        pygame.display.flip()

    def draw(self):
        self.screen.fill(constants.COLOR_BACKGROUND)
        self.screen.blit(self._bg, self._bg.get_rect())

        if self._text_image is not None:
            text_rect = self._text_image.get_rect()
            x = (self.width  / 2) - (text_rect.width  / 2)
            y = (self.height / 2) - (text_rect.height / 2)
            self.screen.blit(self._text_image, (x, y))

    def _exit(self):
        self.running = False

    def _loop(self):
        while self.running:
            for event in pygame.event.get():
                # Make sure we don't handle unnecessary events
                if not self.running:
                    return

                self.event(event)
