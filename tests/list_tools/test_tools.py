import pytest

from list_tools.tools import (get_number_of_elements,
                                  get_min_number, get_max_number)


def test_get_number_of_elements_without_error():
    test_list = [1, 2, 3, 4, 5, 6, 7, 8]
    expected_value = 8
    real_value = get_number_of_elements(test_list)
    assert expected_value == real_value, 'El valor devuelto no es correcto'


def test_get_number_of_elements_with_error():
    test_list = None
    expected_value = 8
    with pytest.raises(TypeError):
        real_value = get_number_of_elements(test_list)


def test_min_number_without_error():
    test_list = [234, 523, 4, 2, 34, 3245, 234, 523, 45, 23, 6]
    expected_value = 2
    real_value = get_min_number(test_list)
    assert expected_value == real_value, 'El valor devuelto no es correcto'


def test_min_number_with_error_not_array():
    test_list = "Hola"
    with pytest.raises(AttributeError):
        real_value = get_min_number(test_list)


#def test_min_number_with_error_not_numbers():
#    test_list = ['2', '33', '1111']
#    expected_value = '2'
#    real_value = get_min_number(test_list)
#    assert expected_value == real_value, 'El valor devuelto no es correcto'

test_cases = [
    {'list': [2, 5, 7, 8, 9, 1], 'expected': 9},
    {'list': [22, 55, 77, 38, 29, 41], 'expected': 77},
    {'list': [4, 6, 7, 53, 32, 43, 5345, 25, 34, 5, 324], 'expected': 5345},
    {'list': [12, 15, 17, 18, 19, 11], 'expected': 19},
]


@pytest.fixture(params=test_cases)
def get_cases(request):
    return request.param


def test_max_number_without_error(get_cases):
    test_list = get_cases['list']
    expected_value = get_cases['expected']
    real_value = get_max_number(test_list)
    assert expected_value == real_value, 'El valor devuelto no es correcto'


def test_max_number_with_error_not_array():
    test_list = "Hola"
    with pytest.raises(AttributeError):
        real_value = get_max_number(test_list)




