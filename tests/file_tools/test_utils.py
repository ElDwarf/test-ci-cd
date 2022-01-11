import os
import pytest

from file_tools.utils import read_file, append_text


@pytest.fixture(autouse=True, scope='module')
def create_dummy_file():
    file_name = 'test_file.txt'
    with open(file_name, 'w') as file:
        file.write('Hola Mundo\n')
        file.write('Esto es un archivo dammy\n')
        file.write('Aca termina el archivo\n')
    yield
    os.remove(file_name)


def test_read_file_without_error():
    expected = "Hola Mundo\nEsto es un archivo dammy\nAca termina el archivo\n"
    body_file = read_file('test_file.txt')
    assert expected == body_file, 'No se obtuvo correctamente el contenido.'


def test_read_file_with_error_not_file():
    with pytest.raises(FileNotFoundError):
        body_file = read_file('test_file_1.txt')


