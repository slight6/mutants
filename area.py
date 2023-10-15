""" Module to define the Area class.
    Areas can be explored by the player
    and/or monsters. """

__author__ = 'Jason Consiglio'
__date__ = '10/10/2023'

import random
import csv
from game_util import log_output as log


class Area:
    def __init__(self, x, y, description, monsters, items, exits):
        """ Initialize the Area class.
            Args:
                x (int): The X coordinate of the area.
                y (int): The Y coordinate of the area.
                description (str): The description of the area.
                monsters (list): The monsters in the area.
                items (list): The items in the area.
                exits (list): The exits from the area.
            Returns:
                None
        """
        self.x = x
        self.y = y
        self.description = description
        self.monsters = monsters
        self.items = items
        self.exits = exits
    

    def __str__(self):
        """ String representation of the Area class.
            Args:
                None
            Returns:
                None
        """
        return (
            f'Coordinates: ({self.x}, {self.y})\n'
            f'Description: {self.description}\n'
            f'Monsters: {self.monsters}\n'
            f'Items: {self.items}\n'
            f'Exits: {self.exits}'
        )
    

    @staticmethod
    def get_area(coordinates):
        """ Get an area by coordinates.
            Args:
                coordinates (tuple): The coordinates of the area to get.
            Returns:
                area (Area): The area at the specified coordinates.
        """
        x, y = map(int, coordinates.split(','))
        with open('map.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['coordinates'] == coordinates:
                    return Area(x, y, row['description'], row['monsters'], row['items'], row['exits'])


    @staticmethod
    def get_random_area():
        """ Get a random area.
            Args:
                None
            Returns:
                area (Area): A random area.
        """
        with open('map.csv', mode='r') as file:
            reader = csv.DictReader(file)
            areas = []
            for row in reader:
                areas.append(row)
            area = random.choice(areas)
            x, y = map(int, area['coordinates'].split(','))
            return Area(x, y, area['description'], area['monsters'], area['items'], area['exits'])
    

    def create_area(coordinates, description, monsters, items, exits):
        """ Create a new area.
            Args:
                coordinates (tuple): The coordinates of the area.
                description (str): The description of the area.
                monsters (list): The monsters in the area.
                items (list): The items in the area.
                exits (list): The exits from the area.
            Returns:
                area (Area): The area created.
        """
        area = Area(coordinates, description, monsters, items, exits)
        return area
    

    def create_test_area():
        """ Create a test area.
            Args:
                None
            Returns:
                area (Area): The test area created.
        """
        area = Area((0, 0), 'You are in a dark room.', [], [], [])
        return area
    

    def get_coordinates(self):
        """ Get the coordinates of an area.
            Args:
                None
            Returns:
                coordinates (tuple): The coordinates of the area.
        """
        return self.coordinates
    

    