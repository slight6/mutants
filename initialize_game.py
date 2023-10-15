""" This is to initialize a completely new map and all data files. 
    This is a one-time use script. """

import sys
import logging
import pathlib
import csv
import math
from game_util import log_output as log
from map_util import create_map, open_map
from area_util import create_area

def main():
    """ Main entrypoint into the game.
        Args:
            None
        Returns:
            None
    """
    map_file_name = input('Enter a name for the map file_name: ')
    map_file_name = map_file_name + '.csv'
    print(create_map(map_file_name))
    pass



if __name__ == '__main__':
    main()