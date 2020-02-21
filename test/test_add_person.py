# -*- coding: utf-8 -*-

from model.person import Person


def test_add_person(app, json_persons):
    pers = json_persons
    print(pers.get_data_as_string_for_log())
    old_persons = app.person.get_person_list()
    app.person.create(pers)
    assert len(old_persons) + 1 == app.person.count()
    new_persons = app.person.get_person_list()
    old_persons.append(pers)
    assert sorted(old_persons, key=Person.id_or_max) == sorted(new_persons, key=Person.id_or_max)
