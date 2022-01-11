import pytest

from list_tools.tools import (get_number_of_elements,
                                  get_min_number, get_max_number)

test_cases = [
    {'list': [2, 5, 7, 8, 9, 1],
     'max_expected': 2,
     'min_expected': 1,
     'len_expected': 6},
    {'list': [22, 55, 77, 38, 29, 41],
     'max_expected': 77,
     'min_expected': 22,
     'len_expected': 6},
    {'list': [4, 6, 7, 53, 32, 43, 5345, 25, 34, 5, 324],
     'max_expected': 5345,
     'min_expected': 4,
     'len_expected': 11},
    {'list': [12, 15, 17, 18, 19, 11],
     'max_expected': 19,
     'min_expected': 11,
     'len_expected': 6},
]


@pytest.fixture(params=test_cases)
def get_cases(request):
    return request.param



def test_get_number_of_elements_without_error(get_cases):
    test_list = get_cases['list']
    expected_value = get_cases['len_expected']
    real_value = get_number_of_elements(test_list)
    assert expected_value == real_value, 'El valor devuelto no es correcto'


def test_get_number_of_elements_with_error():
    test_list = None
    with pytest.raises(TypeError):
        real_value = get_number_of_elements(test_list)


def test_min_number_without_error(get_cases):
    test_list = get_cases['list']
    expected_value = get_cases['min_expected']
    real_value = get_min_number(test_list)
    assert expected_value == real_value, 'El valor devuelto no es correcto'


def test_min_number_with_error_not_array():
    test_list = "Hola"
    with pytest.raises(AttributeError):
        real_value = get_min_number(test_list)


def test_min_number_with_error_empty_array():
    test_list = []
    with pytest.raises(IndexError):
        real_value = get_min_number(test_list)



def test_max_number_without_error(get_cases):
    test_list = get_cases['list']
    expected_value = get_cases['max_expected']
    real_value = get_max_number(test_list)
    assert expected_value == real_value, 'El valor devuelto no es correcto'


def test_max_number_with_error_not_array():
    test_list = "Hola"
    with pytest.raises(AttributeError):
        real_value = get_max_number(test_list)


def test_max_number_with_error_empty_array():
    test_list = []
    with pytest.raises(IndexError):
        real_value = get_max_number(test_list)

