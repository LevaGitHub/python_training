import string
import fixture.general as general
from model.person import Person
from model.group import Group
from fixture.orm import ORMFixture
import random


def checking_preconditions_before_add_group(app, db):
    if len(db.get_person_list()) == 0:
        app.person.create(Person(firstname='please', middlename='add', lastname='me_to_group'))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='for_test_add_person_to_group'))


def test_add_person_to_group(app):
    db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    checking_preconditions_before_add_group(app, db)
    all_persons = db.get_person_list()
    edited_person = random.choice(all_persons)
    print("person - {}".format(edited_person.lastname))
    all_groups = db.get_group_list()
    group_to_add = random.choice(all_groups)
    print("group - {}".format(group_to_add))
    persons_groups = db.get_group_in_person(edited_person)
    assert group_to_add not in persons_groups
    app.person.add_person_to_group(edited_person, group_to_add.name)
    persons_groups = db.get_group_in_person(edited_person)
    assert group_to_add in persons_groups
