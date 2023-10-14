""" Main entrypoint into the game. """

import sys
import logging
import pathlib
import csv
import math

def main():
    """ Main entrypoint into the game.
        Args:
            None
        Returns:
            None
    """
    LOG_FORMAT = '%(levelname)s %(asctime)s - %(message)s'
    logging.basicConfig(filename='main-log.log',
                        level=logging.DEBUG,
                        format=LOG_FORMAT,)
    logger = logging.getLogger()
    logger.debug('Just a debug message')
    logger.info('Just an info message')
    logger.warning('not now John, I have got to get on with the show')
    logger.error('Did you think you were going to divide by zero here?')
    logger.critical('The whole thing is going to blow up now')


    pass


def quadratic_formula(a, b, c):
    """ Returns the solutions to the equation ax^2 + bx + c = 0.
        Args:
            a (float): Coefficient of x^2
            b (float): Coefficient of x
            c (float): Constant
        Returns:
            tuple: The two solutions
    """
    LOG_FORMAT = '%(levelname)s %(asctime)s - %(message)s'
    logging.basicConfig(filename='main-log.log',
                        level=logging.DEBUG,
                        format=LOG_FORMAT,)
    logger = logging.getLogger()
    logger.info('quadratic_formula({0}, {1}, {2})'.format(a, b, c))
    disc = b**2 - 4*a*c
    root1 = (-b + math.sqrt(disc)) / (2*a)
    root2 = (-b - math.sqrt(disc)) / (2*a)
    return (root1, root2)
    roots = quadratic_formula(1, 0, -4)
    logging.debug(roots)
    pass

if __name__ == '__main__':
    main()
