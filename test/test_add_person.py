# -*- coding: utf-8 -*-

from model.person import Person


def test_add_person(app, json_persons, db):
    pers = json_persons
    print(pers.get_data_as_string_for_log())
    old_persons = db.get_person_list()
    app.person.create(pers)
    new_persons = db.get_person_list()
    assert len(old_persons) + 1 == len(new_persons)
    old_persons.append(pers)
    assert sorted(old_persons, key=Person.id_or_max) == sorted(new_persons, key=Person.id_or_max)
