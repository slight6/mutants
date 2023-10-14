""" Map utility functions like create_map, load_map, save_map, etc. """

__author__ = 'Jason Consiglio'
__date__ = '10/10/2018'

import sys
import logging
import pathlib
import csv
import random
from game_util import log_output as log
from monster_util import create_monster
from monster_util import Monster

def create_map(file_name):
    """ Creates a new 99 x 99 map of rooms to explore.
        Args:
            file_name (str): The name of the map file to create.
        Returns:
            success_message (str): A message indicating the map was created.
    """
    
    with open(file_name, 'w', newline='') as map_file:
        map_writer = csv.writer(map_file, delimiter=',')
        monster = 0
        # This is obviously a simple implementation.  We'll want to make this more complex later.
        for x in range(-49, 49, 1):
            for y in range(-49, 49, 1):
                monster_info = Monster()
                if random.randint(1, 100) > 80:
                    map_writer.writerow([x, y, monster_info.name, monster_info.health, monster_info.attack, monster_info.defense, monster_info.speed, monster_info.magic, monster_info.gold, monster_info.experience, monster_info.level])
                else:
                    map_writer.writerow([x, y])
    return 'Map created successfully.'
    

def open_map(year_requested):
    """ Opens a map.
        Args:
            year_requested (int): The year of the map to open.
        Returns:
            map
    """
    pass

