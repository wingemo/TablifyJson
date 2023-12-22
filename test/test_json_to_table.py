import pytest
from src.main import json_to_table

def test_simple_dict():
    json_str = '{"namn": "Erik", "ålder": 40}'
    result = json_to_table(json_str)
    assert len(result) == 1
    assert result['namn'][0] == 'Erik'
    assert result['ålder'][0] == 40

def test_list_of_dicts():
    json_str = '[{"namn": "Anna", "ålder": 30}, {"namn": "Berit", "ålder": 25}]'
    result = json_to_table(json_str)
    assert len(result) == 2
    assert result['namn'][0] == 'Anna'
    assert result['ålder'][1] == 25

def test_complex_nested_dict():
    json_str = '{"person": {"namn": "Erik", "ålder": 40, "adress": {"gata": "Huvudgatan 1", "stad": "Storstad"}}}'
    result = json_to_table(json_str)
    assert len(result) == 1
    assert result['person.namn'][0] == 'Erik'
    assert result['person.adress.stad'][0] == 'Storstad'

def test_invalid_json():
    json_str = 'Inte en JSON-sträng'
    with pytest.raises(ValueError):
        json_to_table(json_str)

def test_empty_json():
    json_str = '{}'
    result = json_to_table(json_str)
    assert result.empty

def test_empty_list():
    json_str = '[]'
    result = json_to_table(json_str)
    assert result.empty

def test_dict_of_lists():
    json_str = '{"namn": ["Ola", "Karin"], "ålder": [35, 45]}'
    result = json_to_table(json_str)
    assert len(result) == 2
    assert result['namn'][1] == 'Karin'
    assert result['ålder'][0] == 35
