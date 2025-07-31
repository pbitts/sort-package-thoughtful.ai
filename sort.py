import logging

from config import *


def sort(width: float, height: float, lenght: float, mass: float) -> str:
    """
    Sort package to its stack.

    :param width:
        (float) Package's width
    :param height:
        (float) Package's height
    :param lenght:
        (float) Package's lenght
    :param mass:
        (float) Package's mass
    
    :return: string indicating corresponding stack
    """

    logger = logging.getLogger(sort.__qualname__)
    logger.info('Sorting packages...')

    heavy = is_heavy(mass)
    bulky = is_bulky(width, height, lenght)

    logger.info(f'Package Heavy={heavy} and Bulky={bulky}')

    if heavy and bulky:
        return REJECTED_STACK
    elif (heavy and not bulky) or (bulky and not heavy):
        return SPECIAL_STACK
    else:
        return STANDARD_STACK
    
def is_heavy(mass: float) -> bool:
    """
    Checks if package's mass is considered heavy

    :param mass:
        (float) Package's mass
    :return: bool indicating if mass is considered heavy
    """
    return mass >= HEAVY_MASS

def is_bulky(width: float, height: float, lenght: float) -> bool:
    """
    Checks if package's volume or one of its dimensions is considered bulky

    :param width:
        (float) Package's width
    :param height:
        (float) Package's height
    :param lenght:
        (float) Package's lenght

    :return: bool indicating if volume or one of its dimensions is considered bulky
    """

    def is_min_bulky_dimension(dimension: float) -> bool:
        return dimension >= BULKY_MIN_DIMENSION
    
    def is_bulky_volume(width: float, height: float, lenght: float) -> bool:
        return width * height * lenght >= BULKY_VOLUME
        
    return is_bulky_volume(width, height, lenght) or \
            is_min_bulky_dimension(width) or \
            is_min_bulky_dimension(height) or \
            is_min_bulky_dimension(lenght)
