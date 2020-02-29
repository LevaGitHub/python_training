import string
import fixture.general as general
from model.person import Person
import random


def checking_preconditions_before_delete(app, db):
    if len(db.get_person_list()) == 0:
        app.person.create(Person(firstname='please', middlename='edit', lastname='me'))


def test_edit_person(app, db, check_ui):
    checking_preconditions_before_delete(app, db)
    pers = Person(firstname=general.generate_sequence(20, string.ascii_letters),
                  middlename=general.generate_sequence(20, string.ascii_letters),
                  lastname=general.generate_sequence(20, string.ascii_letters),
                  nickname=general.generate_sequence(20, string.ascii_letters),
                  title=general.generate_sequence(20, string.ascii_letters),
                  company=general.generate_sequence(20, string.ascii_letters),
                  address=general.generate_sequence(20, string.ascii_letters),
                  home=general.generate_sequence(2, string.digits),
                  mobile=general.generate_sequence(11, string.digits),
                  work=general.generate_sequence(20, string.ascii_letters),
                  fax=general.generate_sequence(11, string.digits),
                  email=general.generate_sequence(20, string.ascii_letters),
                  email2=general.generate_sequence(20, string.ascii_letters),
                  email3=general.generate_sequence(20, string.ascii_letters),
                  homepage=general.generate_sequence(20, string.ascii_letters),
                  bday=general.choice(general.days),
                  bmonth=general.choice(general.months),
                  byear=general.choice(general.years),
                  aday=general.choice(general.days),
                  amonth=general.choice(general.months),
                  ayear=general.choice(general.years),
                  address2=general.generate_sequence(20, string.ascii_letters),
                  phone2=general.generate_sequence(11, string.digits),
                  notes=general.generate_sequence(50, string.ascii_letters))
    old_persons = db.get_person_list()
    edit_person = random.choice(old_persons)
    pers.person_id = edit_person.person_id
    app.person.edit_person_by_id(pers)
    new_persons = db.get_person_list()
    assert len(old_persons) == len(new_persons)
    old_persons.remove(edit_person)
    edit_person.edit(pers)
    old_persons.append(edit_person)
    assert sorted(old_persons, key=Person.id_or_max) == sorted(new_persons, key=Person.id_or_max)
    if check_ui:
        assert sorted(new_persons, key=Person.id_or_max) == sorted(app.person.get_person_list(), key=Person.id_or_max)
