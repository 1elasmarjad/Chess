import constants
import pygame


class controller:
    tiles = []

    @classmethod
    def add(cls, tile):
        cls.tiles.append(tile)

    @classmethod
    def in_a_tile(cls, mouse_x, mouse_y):
        for t in cls.tiles:
            if t.in_tile(mouse_x, mouse_y):
                return t
        return False


class tile:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        controller.add(self)

    def in_tile(self, mouse_x, mouse_y):
        if self.x < mouse_x < self.x + constants.TILE_SIZE and \
                self.y < mouse_y < self.y + constants.TILE_SIZE:
            return True
        return False

    def hover_effect(self, display):
        hover_img = pygame.image.load(constants.HOVER_EFFECT_PATH)
        display.blit(hover_img, (self.x, self.y))

    def grid_pos(self):
        return int(self.x/constants.TILE_SIZE), int(self.y/constants.TILE_SIZE)
