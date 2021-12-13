"""
This library contains the functions and classes to take the obstacles related to floor2
"""
import math

from Graph import GridWithWeights

def calc_grid_position(index, min_position, resolution):
    pos = index * resolution + min_position
    return pos

def comp_grid_position(pos, min_pos, grid_res, robot_radius):
    """
    Given the obstacle position it computes the index inside the grid
    pos: Float Array, [x_obstacle_dot, y_obstacle_dot]
    min_pos: Float Array, [min(x_obstacles), min(y_obstacles)]
    grid_res: Float, the grid resolution (example 0.1)
    robot_radius: Float
    """
    x = int(round((pos[0]-min_pos[0])/grid_res))
    y = int(round((pos[1]-min_pos[1])/grid_res))
    out = []
    for ix in range(x - robot_radius/grid_res , x + robot_radius/grid_res):
        for iy in range(y - int(robot_radius/grid_res + 1) , y + int(robot_radius/grid_res + 1)):
            d = math.hypot(ix - x, iy - y)
            if d < robot_radius/grid_res:
                out.append((ix, iy))
    return out
def calc_obstacle_map(ox, oy, resolution):
    """
    Given the obstacles, it computes the grid map in the format compatible with the previous 
    """
    rr = 0.25
    min_x = round(min(ox))
    min_y = round(min(oy))
    max_x = round(max(ox))
    max_y = round(max(oy))
    print("min_x:", min_x)
    print("min_y:", min_y)
    print("max_x:", max_x)
    print("max_y:", max_y)

    x_width = int(round((max_x - min_x) / resolution))#
    y_width = int(round((max_y - min_y) / resolution))#
    print("x_width:", x_width)
    print("y_width:", y_width)

    # obstacle map generation
    obstacle_map = [[False for _ in range(y_width)]
                            for _ in range(x_width)]
    for ix in range(x_width):
        x = calc_grid_position(ix, min_x)
        for iy in range(y_width):
            y = calc_grid_position(iy, min_y)
            for iox, ioy in zip(ox, oy):
                d = math.hypot(iox - x, ioy - y)
                if d <= rr:
                    obstacle_map[ix][iy] = True
                    break
    
    return obstacle_map

def generate_grid(ox, oy, grid_res):
    min_x = round(min(ox))
    min_y = round(min(oy))
    max_x = round(max(ox))
    max_y = round(max(oy))
    print("min_x:", min_x)
    print("min_y:", min_y)
    print("max_x:", max_x)
    print("max_y:", max_y)

    x_width = int(round((max_x - min_x) / grid_res))#
    y_width = int(round((max_y - min_y) / grid_res))#
    print("x_width:", x_width)
    print("y_width:", y_width)

    grid = GridWithWeights(x_width, y_width)

    for (iox, ioy) in zip(ox, oy):
        grid.walls += comp_grid_position([iox,ioy], [min_x,min_y], grid_res, 0.25)
    

    