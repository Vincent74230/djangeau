"""Starting point of the app"""
from . import tools
from config import WATER


def main():
    """Main function of the app"""
    tools.water_plants(WATER)

if __name__ == '__main__':
    main()
