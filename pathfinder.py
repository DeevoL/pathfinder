import pygame
import object_grid
import sys
import cProfile
import copy

def main():
    global min_dist
    global min_square
    pygame.init()
    white = (255, 255, 255)
    green = (57, 205, 130)
    grey = (80, 80, 80)
    blue = (143,193,229)
    purple = (239,136,240)
    orange = (241,163,77)
    mode = 'draw'
    screen_x = 1280
    screen_y = 720
    square_outline_width = 2
    square_length = 16
    total_square_length = 2 * square_outline_width + square_length
    screen = pygame.display.set_mode([screen_x,screen_y])
    start_square = None
    end_square = None
    min_dist = 999
    min_square = []
    square_queue = []
    clock = pygame.time.Clock()

    grid = [[] for i in range(int(screen_x/total_square_length))]
    for x,x_ele in enumerate(grid):
        for y in range(int(screen_y/total_square_length)):
            grid[x].append(object_grid.square(screen,screen_x,screen_y,x,y,square_length,square_outline_width))

    for col in grid:
        for row,row_ele in enumerate(col):
            row_ele.clear()

    def adj_check(ref_square, adj_square):
        global min_dist 
        global min_square 
        if not(adj_square.is_wall):
            if adj_square.dist_from_start > ref_square.dist_from_start + adj_square.cost:
                adj_square.dist_from_start = ref_square.dist_from_start + adj_square.cost
            if not (adj_square.checked):
                square_queue.append(adj_square)
                adj_square.checked = True
            if adj_square.dist_from_start < min_dist:
                min_dist = adj_square.dist_from_start
                min_square[:] = adj_square.path_to_square[:]
            if adj_square.get_coords() != start_square.get_coords():
                g = adj_square.dist_from_start * 2 + 20
                if g > 245 :
                    g = 245
                adj_square.fill((22, 255 - g, 200))
        



    while True:
        pressed = pygame.key.get_pressed()
        mouse_square = grid[pygame.mouse.get_pos()[0]//total_square_length][
                        pygame.mouse.get_pos()[1]//total_square_length]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT:
                    if mode == 'draw':
                        mode = 'erase'
                    else:
                        mode = 'draw'

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    for square in grid:
                        for y,ele in enumerate(square):
                            square[y].clear()
                    start_square = None
                    end_square = None
                    end_found = False
                    end_count = 0
                    square_queue = []
                    

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    if start_square != None:
                        start_square.clear()
                    start_square = mouse_square 
                    mouse_square.fill((241,130,241))
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    if end_square != None:
                        end_square.clear()
                    end_square = mouse_square
                    end_square.clear()
                    mouse_square.is_end = True 
                    mouse_square.fill((221,94,50))
                           
            if pygame.mouse.get_pressed()[0] == True:
                if mode == 'draw':
                    mouse_square.fill(green)
                    mouse_square.is_wall = False
                elif mode == 'erase':
                    mouse_square.clear()

            if pygame.mouse.get_pressed()[2] == True:
                if mode == 'draw':
                    mouse_square.clear()
                    mouse_square.fill(grey)
                    mouse_square.is_wall = True
                    mouse_square.cost = sys.maxsize
                elif mode == 'erase':
                    mouse_square.clear()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    if mode == 'draw':
                        mouse_square.clear()
                        mouse_square.fill((18,63,10))
                        mouse_square.cost = 2
                    elif mode == 'erase':
                        mouse_square.clear()


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    temp_queue = []
                    square_queue.append(start_square)
                    start_square.dist_from_start = 0
                    start_square.cost = 0
                    
                        
                    while len(square_queue) != 0:
                        pygame.display.flip()
                        current_square = square_queue.pop(0)
                        current_square.checked = True
                        adj_squares = []

                        
                        if current_square.get_x() + 1 != int(screen_x/total_square_length):
                            square_to_right = grid[current_square.get_x()+1][current_square.get_y()]
                            adj_squares.append(square_to_right)
                        if not(current_square.get_x() - 1 < 0):
                            square_to_left = grid[current_square.get_x()-1][current_square.get_y()]
                            adj_squares.append(square_to_left)
                        if not (current_square.get_y() - 1 < 0):
                            square_above = grid[current_square.get_x()][current_square.get_y() - 1]
                            adj_squares.append(square_above)
                        if current_square.get_y() + 1 != int(screen_y/total_square_length):
                            square_below = grid[current_square.get_x()][current_square.get_y() + 1]
                            adj_squares.append(square_below)

                        min_dist = 999
                        min_square = []
                        for square in adj_squares:
                            adj_check(current_square, square)
                            
                        if current_square.get_coords() != start_square.get_coords():
                            start_square.path_to_square = []
                            current_square.path_to_square = min_square
                            if current_square.get_coords() != end_square.get_coords():
                                current_square.path_to_square.append(current_square) 
            
                        if current_square.get_coords() == end_square.get_coords():
                            for square_in_path in end_square.path_to_square:
                                try:
                                    square_in_path.fill(orange)
                                except:
                                    pass
                            end_square.fill((221,94,50))
                            break

        pygame.display.flip()
        clock.tick(120)


main()