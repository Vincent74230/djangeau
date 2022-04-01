"""Starting point of the app"""
from config import WATER
from . import tools



def main():
    """Main function of the app"""
    print(tools.distance_sensor())
    tools.water_plants(WATER)
    print(tools.distance_sensor())

if __name__ == '__main__':
    main()
