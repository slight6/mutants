""" This module contains the Area class and associated functions. """

__author__ = 'Jason Consiglio'
__date__ = '10/10/2018'

import sys
import logging
import pathlib
import csv
import random
from game_util import log_output as log


area_names = (
    "Enchanted Forest", "Misty Mountains", "Cursed Swamp", "Ancient Ruins",
    "Crystal Caverns", "Lost City", "Shadowy Woods", "Forgotten Temple",
    "Whispering Meadows", "Eerie Graveyard", "Mystical Grove", "Haunted Mansion",
    "Dragon's Lair", "Frostbite Peaks", "Sunken Shipwreck", "Burning Wasteland",
    "Twilight Castle", "Goblin Village", "Elven Sanctuary", "Dwarven Mines",
    "For Sale", "Maintenance Shop"
)

success_message = ('Area created successfully.')

class Area:
    def __init__(self):
        self.name = area_names[random.randint(0, len(area_names) - 1)]
        self.default = 'This is a large, dark area.'

# This is obviously a simple implementation.  We'll want to make this more complex later.
def create_area():
    """ Creates a new area.
        Args:
            None
        Returns:
            area (Area): A new area.
            success_message (str): A message indicating the area was created.
    """

    return Area, success_message
    
