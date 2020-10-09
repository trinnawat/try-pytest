import pytest
from src.module_1.module_1_func import string_to_int


class TestModule1Func(object):
    def test_string_to_int_normal_case(self):
        expected = 123
        actual = string_to_int("123")
        assert actual == expected
