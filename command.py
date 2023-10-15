""" Module to define the Command class.
    Commands are classified as either actions or directions.
    Monsters are also able to use commands. """

__author__ = 'Jason Consiglio'
__date__ = '10/10/2023'

import random
import csv
from game_util import log_output as log


class Command:
    def __init__(self, command):
        """ Initialize the Command class.
            Args:
                command (str): The command to initialize.
            Returns:
                None
        """
        self.command = command

    
    def __str__(self):
        """ String representation of the Command class.
            Args:
                None
            Returns:
                None
        """
        return f'Command: {self.command}'
    

    def get_command(command):
        """ Get a command by name.
            Args:
                command (str): The name of the command to get.
            Returns:
                command (Command): The command with the specified name.
        """
        with open('commands.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['command'] == command:
                    return Command(row['command'])
                

    def create_command(command, description):
        """ Create a new command.
            Args:
                command (str): The command to create.
                description (str): The description of the command.
            Returns:
                None
        """
        with open('commands.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([command, description])
        return f'Command {command} created successfully.'
    

    def edit_command(command, description):
        """ Edit a command.
            Args:
                command (str): The command to edit.
                description (str): The description of the command.
            Returns:
                None
        """
        with open('commands.csv', mode='r') as file:
            reader = csv.DictReader(file)
            commands = []
            for row in reader:
                if row['command'] == command:
                    commands.append(row)
            command = random.choice(commands)
        with open('commands.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([command, description])
        return f'Command {command} edited successfully.'