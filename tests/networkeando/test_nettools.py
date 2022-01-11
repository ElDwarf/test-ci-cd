import pytest
import requests

from networkeando.nettools import get_url


class GetResponseDummy:
    def __init__(self, status_code, text):
        self.status_code = status_code
        self.text = text


def test_get_url_without_error_test_status_code(mocker):
    response = GetResponseDummy(200, 'HelloWorld')
    mocker.patch.object(requests, "get", return_value=response)
    expect_status_code = 200
    status_code, _ = get_url('http://www.dominio.com')
    assert expect_status_code == status_code, 'El codigo de estado es incorrecto'


def test_get_url_without_error_test_text(mocker):
    response = GetResponseDummy(200, 'HelloWorld')
    mocker.patch.object(requests, "get", return_value=response)
    expect_text = 'HelloWorld'
    _, text_actual = get_url('http://www.dominio.com')
    assert expect_text == text_actual, 'El codigo de estado es incorrecto'


def test_get_url_without_error_test_status_code_not_200_body_none(mocker):
    response = GetResponseDummy(404, 'HelloWorld')
    mocker.patch.object(requests, "get", return_value=response)
    expect_text = None
    _, text_actual = get_url('http://www.dominio.com')
    assert expect_text == text_actual, 'El codigo de estado es incorrecto'

