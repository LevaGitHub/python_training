# -*- coding: utf-8 -*-
from model.person import Person


def test_delete_first_person(app):
    if app.person.count() == 0:
        app.person.create(Person(firstname='please', middlename='delete', lastname='me'))
    app.person.delete_first_person()
