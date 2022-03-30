"""Starting point of the app"""
from . import tools
from config import WATER


def main():
    """Main function of the app"""
    print(tools.distance_sensor())
    tools.water_plants(WATER)
    print(tools.distance_sensor())

if __name__ == '__main__':
    main()
