# -*- coding: utf-8 -*-
from model.person import Person
import random


def checking_preconditions_before_delete(app, db):
    if len(db.get_person_list()) == 0:
        app.person.create(Person(firstname='please', middlename='delete', lastname='me'))


def test_delete_person(app, db, check_ui):
    checking_preconditions_before_delete(app, db)
    old_persons = db.get_person_list()
    del_person = random.choice(old_persons)
    app.person.delete_person_by_id(del_person.person_id)
    new_persons = db.get_person_list()
    assert len(old_persons) - 1 == len(new_persons)
    old_persons.remove(del_person)
    assert old_persons == new_persons
    if check_ui:
        assert sorted(new_persons, key=Person.id_or_max) == sorted(app.person.get_person_list(), key=Person.id_or_max)
