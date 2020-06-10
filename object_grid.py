import pygame
import sys

class square:

    def __init__(self, surface, screen_x, screen_y, x_coord, y_coord, length, border):
        self.surface = surface
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.screen_x = screen_x
        self.screen_y = screen_y
        self.length = length
        self.border = border
        self.dist_from_start = 999
        self.path_to_square = []
        self.cost = 1
        self.is_end = False
        self.checked = False
        self.is_wall = False
        self.total_square_length = 2 * border + length
        self.rect = pygame.Rect(
                    self.total_square_length * x_coord + 2,
                    self.total_square_length * y_coord + 2,
                    length, length)
    
    def get_coords(self):
        return(self.x_coord,self.y_coord)

    def get_x(self):
        return self.x_coord
    
    def get_y(self):
        return self.y_coord
    
    
    def fill(self,color):
        self.surface.fill(color,self.rect)

    def clear(self):
        self.surface.fill((244,230,150), self.rect)
        self.is_wall = False
        self.cost = 1
        self.is_end = False
        self.checked = False
        self.path_to_square = []
        self.dist_from_start = 999

        

# grid = [[] for i in range(10)]
# for x in range(10):
#     for y in range(10):
#         grid[x].append(square(x,y))

# grid[2][4].get_coords()