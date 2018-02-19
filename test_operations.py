from inputlist import InputList
import logging
from logging_config import config
import pytest
import mock
from badnumbersexception import BadNumbersException

# init logging config
logging.basicConfig(**config)
logger = logging.getLogger(__name__)


def test_import():
    logger.debug('Begin testing import')
    # remove the numpy library
    with mock.patch.dict('sys.modules', {'numpy': None}):
        with pytest.raises(ImportError):
            InputList.import_modules()
    logger.debug('Complete testing import')


def test_check_inputs():
    logger.debug('Begin testing check inputs function')
    error_input_list = (12,
                        [1, 2, 3.32],
                        [4, 'GTHC', 2, 333],
                        [85, -23, -2222222222222],
                        [33, 9001, -2],
                        [-9001],
                        [123, 3, 4, 321])

    error_output_list = (TypeError, TypeError, TypeError,
                         ValueError, ValueError, ValueError,
                         BadNumbersException)
    # loop over exception triggers and module functions
    for i, l in enumerate(error_input_list):
        with pytest.raises(error_output_list[i]):
            InputList(list=l)
    logger.debug('Complete testing check inputs function')


def test_sum():
    logger.debug('Begin testing get_sum method')
    input_lists = ([1, 1],
                   [2, 7001, 5],
                   [-3, 2, 6, 8, 8509])
    input_lists = [InputList(list=x) for x in input_lists]
    output_results = (2, 7008, 8522)
    for i, l in enumerate(input_lists):
        assert l.sum == output_results[i]
    logger.debug('Complete testing sum method')


def test_min_max():
    logger.debug('Begin testing min/max method')
    from inputlist import InputList
    input_lists = ([1, 1],
                   [3, 4, 9],
                   [7, 10, -2, -2])
    input_lists = [InputList(list=x) for x in input_lists]
    output_results = ((1, 1),
                      (3, 9),
                      (-2, 10))
    for i, l in enumerate(input_lists):
        assert l.minmax == output_results[i]
    logger.debug('Complete testing min/max method')


def test_max_diff():
    logger.debug('Begin testing max difference method')
    from inputlist import InputList
    input_lists = ([1, 1, 3],
                   [-1, 3, -16],
                   [5, 5, 5, 5, 5])
    input_lists = [InputList(list=x) for x in input_lists]
    output_results = (2, 4, 0)
    for i, l in enumerate(input_lists):
        assert l.maxdiff == output_results[i]
    logger.debug('Complete testing max difference method')
