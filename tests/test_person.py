from lib.person import Person

def test_person_instantiates():
    person = Person('Hunor', 37)

    assert person.name == 'Hunor'
    assert person.age == 37

def test_person_can_open_door():
    person = Person('Hunor', 37)

    assert person.try_open_door() == True

def test_person_under_5_cant_open_door():
    person = Person('Hunor', 4)

    assert person.try_open_door() == False