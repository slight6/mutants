""" This module contains area utility functions. """

__author__ = 'Jason Consiglio'
__date__ = '10/10/2018'

import sys
import logging
import pathlib
import csv
import random
from game_util import log_output as log


def update_area(coordinates, description, monsters, items, exits):
    """ Update an area in the map.
        Args:
            coordinates (tuple): The coordinates of the area to update.
            description (str): The description of the area.
            monsters (list): The monsters in the area.
            items (list): The items in the area.
            exits (list): The exits from the area.
        Returns:
            success_message (str): A message indicating the area was updated.
    """
    with open('map.csv', mode='r') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        for row in rows:
            if row['coordinates'] == coordinates:
                row['description'] = description
                row['monsters'] = monsters
                row['items'] = items
                row['exits'] = exits
                break
    with open('map.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['coordinates', 'description', 'monsters', 'items', 'exits'])
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    return 'Area updated successfully.'
