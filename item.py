""" Module to define the Item class.
    Items are objects that can be picked up 
    and used by the player or monsters. """

__author__ = 'Jason Consiglio'
__date__ = '10/10/2023'

import random
import csv
import uuid
from game_util import log_output as log

class Item:
    def __init__(self, item_type, name, description, value, weight):
        """ Initialize the Item class.
            Args:
                name (str): The name of the item.
                description (str): The description of the item.
                value (int): The value of the item.
                weight (int): The weight of the item.
            Returns:
                None
        """
        self.uuid = uuid.uuid4()  
        self.name = name
        self.item_type = item_type
        self.description = description
        self.value = value
        self.weight = weight

    def __str__(self):
        """ String representation of the Item class.
            Args:
                None
            Returns:
                None
        """
        return f'UUID: {self.uuid}\nName: {self.name}\nItem Type: {self.item_type}\nDescription: {self.description}\nValue: {self.value}\nWeight: {self.weight}'


def get_random_item(item_type):
    """ Get a random item.
        Args:
            None
        Returns:
            item (Item): A random item.
    """
    with open('items.csv', mode='r') as file:
        reader = csv.DictReader(file)
        items = []
        for row in reader:
            if row['item_type'] == item_type:
                items.append(row)
        item_data = random.choice(items)
        return Item(item_data['item_type'], item_data['name'], item_data['description'], item_data['value'], item_data['weight'])


def get_item(item_name):
    """ Get an item by name.
        Args:
            item_name (str): The name of the item to get.
        Returns:
            item (Item): The item requested.
    """
    with open('items.csv', mode='r') as file:
        reader = csv.DictReader(file)
        items = []
        for row in reader:
            if row['name'] == item_name:
                items.append(row)
        item_data = random.choice(items)
        return Item(item_data['item_type'], item_data['name'], item_data['description'], item_data['value'], item_data['weight'])


def get_item_by_type(item_type):
    """ Get an item by type.
        Args:
            item_type (str): The type of item to get.
        Returns:
            item (Item): The item requested.
    """
    with open('items.csv', mode='r') as file:
        reader = csv.DictReader(file)
        items = []
        for row in reader:
            if row['item_type'] == item_type:
                items.append(row)
        item_data = random.choice(items)
        return Item(item_data['item_type'], item_data['name'], item_data['description'], item_data['value'], item_data['weight'])


def get_item_by_value(value):
    """ Get an item by value.
        Args:
            value (int): The value of the item to get.
        Returns:
            item (Item): The item requested.
    """
    with open('items.csv', mode='r') as file:
        reader = csv.DictReader(file)
        items = []
        for row in reader:
            if row['value'] == value:
                items.append(row)
        item_data = random.choice(items)
        return Item(item_data['item_type'], item_data['name'], item_data['description'], item_data['value'], item_data['weight'])


def get_item_by_weight(weight):
    """ Get an item by weight.
        Args:
            weight (int): The weight of the item to get.
        Returns:
            item (Item): The item requested.
    """
    with open('items.csv', mode='r') as file:
        reader = csv.DictReader(file)
        items = []
        for row in reader:
            if row['weight'] == weight:
                items.append(row)
        item_data = random.choice(items)
        return Item(item_data['item_type'], item_data['name'], item_data['description'], item_data['value'], item_data['weight'])


def create_item(item_type, name, description, value, weight):
    """ Create a new item.
        Args:
            item_type (str): The type of item to create.
            name (str): The name of the item to create.
            description (str): The description of the item to create.
            value (int): The value of the item to create.
            weight (int): The weight of the item to create.
        Returns:
            item (Item): The item requested.
    """
    with open('items.csv', mode='a', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow([uuid.uuid4(), item_type, name, description, value, weight])
    return Item(item_type, name, description, value, weight)
