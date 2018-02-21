import numpy as np
import logging
from logging_config import config
from badnumbersexception import BadNumbersException

logging.basicConfig(**config)
logger = logging.getLogger(__name__)


class InputList():

    def __init__(self, list=None, sum=None, minmax=None, maxdiff=None):
        self.list = list
        self.sum = sum
        self.minmax = minmax
        self.maxdiff = maxdiff
        self.get_sum()
        self.get_min_max()
        self.get_max_diff()

    def get_sum(self):
        """ Returns the sum of a list

        :param self: list of n integers between -9,000 and 9,000
        :returns: sum of all the n integers in the list
        :raises TypeError: Input must be lists
        :raises TypeError: Input elements must be integers
        :raises ValueError: All input elements must be between -9,000 and 9,000 (inclusive)
        :raises BadNumbersException: Numbers 123 and 321 cannot be in same list
        """
        logger.info('Calculating sum of the list')
        logger.debug('Input list: %s', str(self.list))
        try:
            self.check_inputs()
        except TypeError:
            logger.error("TypeError in get_sum, must be list of integers")
        except ValueError:
            logger.error("ValueError in get_sum, integers must be between -9,000 and 9,000")
        self.check_inputs()
        logger.debug('Output: %s', sum(self.list))
        self.sum = sum(self.list)

    def get_min_max(self):
        """ Returns min and max in a list

        :param self: (int) list to get min and max of
        :returns: min and max of list in a tuple
        :raises TypeError: Input must be lists
        :raises TypeError: Input elements must be integers
        :raises ValueError: All input elements must be between -9,000 and 9,000 (inclusive)
        :raises BadNumbersException: Numbers 123 and 321 cannot be in same list
        """
        logger.info('Obtaining min and max of list')
        logger.debug('Input list: %s', str(self.list))
        try:
            self.check_inputs()
        except TypeError:
            logger.error("TypeError in get_min_max, must be list of integers")
        except ValueError:
            logger.error("ValueError in get_min_max, must be between -9,000 and 9,000")
        self.check_inputs()
        np = self.import_modules()
        min_max = (np.amin(self.list), np.amax(self.list))
        logger.debug('Output: %s', str(min_max))
        self.minmax = min_max

    def get_max_diff(self):
        """ Returns maximum difference between consecutive elements in input list

        :param self: list of n integers between -9,000 and 9,000
        :returns: maximum difference d defined by d = self[i+1] - self[i] for i = 0 to n-1
        :raises ImportError: If Numpy is not installed
        :raises TypeError: Input must be lists
        :raises TypeError: Input elements must be integers
        :raises ValueError: All input elements must be between -9,000 and 9,000 (inclusive)
        :raises BadNumbersException: Numbers 123 and 321 cannot be in same list
        """
        logger.info('Calculating maximum difference in the list')
        logger.debug('Input list: %s', str(self.list))
        try:
            self.check_inputs()
        except TypeError:
            logger.error("TypeError in get_max_diff, must be list of integers")
        except ValueError:
            logger.error("ValueError in get_max_diff, must be between -9,000 and 9,000")
        self.check_inputs()
        np = self.import_modules()
        diff_arr = np.diff(self.list)
        max_diff = np.max(diff_arr)
        logger.debug('Output: %s', str(max_diff))
        self.maxdiff = max_diff

    def check_inputs(self):
        """ Checks if input list fits desired format

        :param self: list of n integers between -9,000 and 9,000
        :raises TypeError: Input must be lists
        :raises TypeError: Input elements must be integers
        :raises ValueError: All input elements must be between -9,000 and 9,000 (inclusive)
        :raises BadNumbersException: Numbers 123 and 321 cannot be in same list
        """

        if not type(self.list) is list:
            logger.error("TypeError in input list: input must be a list")
            raise TypeError('Input must be a list')

        if not all([type(num) is int for num in self.list]):
            logger.error("TypeError in input list: All inputs must be integers")
            raise TypeError('All inputs in list must be integers.')

        if any([abs(num) > 9000 for num in self.list]):
            logger.error("ValueError in get_max_diff, must be between -9,000 and 9,000")
            raise ValueError('All inputs must be between -9,000 and 9,000 (inclusive)')
        elif any([abs(num) > 8500 for num in self.list]):
            logger.warning('Some of your inputs are very close to 9000. Be careful to not exceed 9000!')
        elif any([abs(num) > 7000 for num in self.list]):
            logger.warning('Some of your inputs are somewhat close to 9000. Be careful to not exceed 9000!')

        if 123 in self.list and 321 in self.list:
            raise BadNumbersException('List cannot contain both 123 and 321')

    @staticmethod
    def import_modules():
        """ Imports required module (Numpy)

        :returns: the module Numpy
        """
        try:
            import numpy as np
        except (ModuleNotFoundError, ImportError):
            logger.error('Could not import numpy')
            raise ImportError(
                '''Could not import numpy. Please make sure to have the package installed''')
        logger.info('Imported numpy module')
        return np
