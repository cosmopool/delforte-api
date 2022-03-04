import pytest
from zione.core.utils.dict_utils import capitalize_dict_keys

def test_return_dict_with_one_key_capitalized():
    d = {'a': 1}
    d_cap = capitalize_dict_keys(d)

    assert d_cap['A'] == 1

def test_return_dict_with_more_then_one_key_capitalized():
    d = {'a': 1, 'b': 2}
    d_cap = capitalize_dict_keys(d)

    assert d_cap['A'] == 1
    assert d_cap['B'] == 2

def test_return_dict_with_one_long_key_capitalized():
    d = {'capitalize': 1}
    d_cap = capitalize_dict_keys(d)

    assert d_cap['Capitalize'] == 1

def test_old_key_should_not_exist():
    d = {'a': 1}
    d_cap = capitalize_dict_keys(d)

    with pytest.raises(KeyError):
        assert d_cap['a']
def test_capitalize_more_then_one_key():
    d = {'dog': 0, 'cat': 1, 'horse': 2, 'snake': 3}
    d_cap = capitalize_dict_keys(d)

    assert d_cap['Dog'] == 0
    assert d_cap['Cat'] == 1
    assert d_cap['Horse'] == 2
    assert d_cap['Snake'] == 3
