from lib.house import House
from unittest.mock import Mock

def test_house_instantiates():
    house = House()

    assert house.door_open == False

def test_house_open_door_with_more_than_4_year_old():
    house = House()

    mock_person = Mock()
    mock_person.try_open_door.return_value = True

    house.open_door(mock_person)

    assert house.door_open == True

def test_house_open_door():
    house = House()
    
    mock_person = Mock()
    mock_person.try_open_door.return_value = False

    house.open_door(mock_person)

    assert house.door_open == False