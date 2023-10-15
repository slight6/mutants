""" Map utility functions for the game. """

__author__ = 'Jason Consiglio'
__date__ = '10/10/2018'

import sys
import logging
import pathlib
import csv
import random
from game_util import log_output as log
from game_util import is_prime as is_prime
from monster_util import Monster
from area import Area

import csv

def create_map(file_name):
    """ Creates a new 99 x 99 map of rooms to explore.
        Args:
            file_name (str): The name of the map file to create.
        Returns:
            success_message (str): A message indicating the map was created.
    """
    with open(file_name, 'w', newline='') as map_file:
        fieldnames = ['X Coordinates', 'Y Coordinates', 'Description', 'Monsters', 'Items', 'Exits']  # Define header row
        map_writer = csv.DictWriter(map_file, fieldnames=fieldnames)  # Use DictWriter for better readability
        
        map_writer.writeheader()  # Write the header row
        
        # This is obviously a simple implementation. We'll want to make this more complex later.
        for x in range(-2, 2):  # Adjust range to include 49
            for y in range(-2, 2):  # Adjust range to include 49
                area = Area(x, y, 'This is a test area.', 'monsters', 'items', 'exits')
                map_writer.writerow({
                    'X Coordinates': area.x,
                    'Y Coordinates': area.y,
                    'Description': area.description,
                    'Monsters': area.monsters,
                    'Items': area.items,
                    'Exits': area.exits
                })
    return 'Map created successfully.'


    
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
    """

