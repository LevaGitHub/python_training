# -*- coding: utf-8 -*-

import string
import fixture.general as general
from model.person import Person
import pytest

test_data = [
    Person(firstname=general.generate_sequence(20, general.test_seq, prefix='firstname'),
           middlename=general.generate_sequence(20, general.test_seq, prefix='middlename'),
           lastname=general.generate_sequence(20, general.test_seq, prefix='lastname'),
           nickname=general.generate_sequence(20, general.test_seq),
           title=general.generate_sequence(20, general.test_seq),
           company=general.generate_sequence(20, general.test_seq),
           address=general.generate_sequence(20, general.test_seq),
           home=general.generate_sequence(2, string.digits + string.punctuation),
           mobile=general.generate_sequence(11, string.digits + string.punctuation),
           work=general.generate_sequence(20, general.test_seq),
           fax=general.generate_sequence(11, string.digits + string.punctuation),
           email=general.generate_sequence(20, general.test_seq),
           email2=general.generate_sequence(20, general.test_seq),
           email3=general.generate_sequence(20, general.test_seq),
           homepage=general.generate_sequence(20, general.test_seq),
           bday=general.choice(general.days),
           bmonth=general.choice(general.months),
           byear=general.choice(general.years),
           aday=general.choice(general.days),
           amonth=general.choice(general.months),
           ayear=general.choice(general.years),
           address2=general.generate_sequence(20, general.test_seq),
           phone2=general.generate_sequence(11, string.digits + string.punctuation),
           notes=general.generate_sequence(50, general.test_seq))
    for _ in range(3)
]


@pytest.mark.parametrize("pers", test_data)
def test_add_person(app, pers):
    print(pers.get_data_as_string_for_log())
    old_persons = app.person.get_person_list()
    app.person.create(pers)
    assert len(old_persons) + 1 == app.person.count()
    new_persons = app.person.get_person_list()
    old_persons.append(pers)
    assert sorted(old_persons, key=Person.id_or_max) == sorted(new_persons, key=Person.id_or_max)
