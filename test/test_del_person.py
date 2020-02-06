# -*- coding: utf-8 -*-
from model.person import Person
from random import randrange


def test_delete_first_person(app):
    if app.person.count() == 0:
        app.person.create(Person(firstname='please', middlename='delete', lastname='me'))
    old_persons = app.person.get_person_list()
    index = randrange(len(old_persons))
    app.person.delete_person_by_index(index)
    assert len(old_persons) - 1 == app.person.count()
    new_persons = app.person.get_person_list()
    old_persons[index:index + 1] = []
    assert old_persons == new_persons
