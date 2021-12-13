from Algorithms import *
from Graph import *
import Import_map
import obstacle

def main():
    # came_from, cost_so_far = a_star_search(diagram4, (1, 4), (7, 8))
    ox, oy = obstacle.compute_obstacles("map_plus_3_parks")
    
if __name__ == '__main__':
    main()