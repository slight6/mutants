""" Utility functions for the game. """

import sys
import logging


def log_output(input_message, output_file):
    """ Sets up the logging for the game.
        Args:
            input_log_info (str): The name of the log file.
            output_file (str): The name of the log file.
        Returns:
            None
    """
    if output_file == 'game':
        output_to = 'game.log'
    elif output_file == 'player':
        output_to = 'player.log'
    elif output_file == 'monster':
        output_to = 'monster.log'
    elif output_file == 'map':
        output_to = 'map.log'
    elif output_file == 'item':
        output_to = 'item.log'
    elif output_file == 'room':
        output_to = 'room.log'
    else:
        output_to = 'main.log'
    LOG_FORMAT = '%(levelname)s %(asctime)s - %(message)s'
    logging.basicConfig(filename=output_to,
                        level=logging.DEBUG,
                        format=LOG_FORMAT,)
    logger = logging.getLogger()
    logger.debug(input_message)
    

def is_prime(number):
    """ Checks if a number is prime.
        Args:
            number (int): The number to check.
        Returns:
            True if the number is prime, False otherwise.
    """
    if number == 1:
        return False
    elif number == 2:
        return True
    else:
        for x in range(2, number):
            if number % x == 0:
                return False
        return True