"""Starting point of the app"""
from config import WATER
from . import tools



def main():
    """Main function of the app"""
    water_level = tools.distance_sensor()
    if water_level < 31:
        tools.water_plants(WATER)
        tools.print_in_the_file(water_level)
    else:
        tools.print_in_the_file(water_level)
if __name__ == '__main__':
    main()
