""" Main entrypoint into the game. """

import sys
import logging
import pathlib
import csv
import math
from game_util import log_output as log
from map_util import create_map, open_map

def main():
    """ Main entrypoint into the game.
        Args:
            None
        Returns:
            None
    """
    map_file_name = input('Enter a name for the map file_name: ')
    map_file_name = map_file_name + '.csv'
    create_map(map_file_name)
    pass



if __name__ == '__main__':
    main()
