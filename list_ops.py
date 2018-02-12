try:
    import numpy as np
except ImportError:
    raise ImportError('''Could not import numpy. Please make sure to have the
                      package installed''')


def get_sum(input_list):
    check_inputs(input_list)
    '''
    Returns the sum of a list
    '''
    return sum(input_list)


def get_min_max(input_list):
    check_inputs(input_list)
    min_max = (np.amin(input_list), np.amax(input_list))
    return min_max


def get_max_diff(input_list):
    '''
    Returns maximum difference between consecutive elements in input list
    :param input_list: list of n integers between -9,000 and 9,000
    :return : returns maximum difference d defined by d = input_list[i+1] -
    input_list[i] for i = 0 to n-1
    :raise ImportError: Numpy or other package not installed
    :raise TypeError: Input must be lists
    :raise TypeError: Input elements must be integers
    :raise ValueError: All input elements must be between -9,000 and
    9,000
    '''
    check_inputs(input_list)
    diff_arr = np.diff(input_list)
    max_diff = np.max(diff_arr)
    return max_diff


def check_inputs(input_list):
    if(not type(input_list) is list):
        raise TypeError('Input must list')
    if(not all([type(num) is int for num in input_list])):
        raise TypeError('All inputs in list must be integers.')
    if(any([abs(num) > 1000000 for num in input_list])):
        raise ValueError('All inputs must be between -9,000 and 9,000')
