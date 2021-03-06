# -*- coding: utf-8 -*-

from pony.orm import *
from datetime import datetime
from model.group import Group
from model.person import Person


class ORMFixture:

    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')
        persons = Set(lambda: ORMFixture.ORMPerson, table="address_in_groups", column="id", reverse="groups",
                      lazy=True)

    class ORMPerson(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        deprecated = Optional(datetime, column='deprecated')
        groups = Set(lambda: ORMFixture.ORMGroup, table="address_in_groups", column="group_id", reverse="persons",
                     lazy=True)

    def __init__(self, host, name, user, password):
        self.db.bind('mysql', host=host, database=name, user=user, password=password)
        self.db.generate_mapping()
        sql_debug(True)

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id),
                         name=group.name,
                         header=group.header,
                         footer=group.footer)
        return list(map(convert, groups))

    def convert_persons_to_model(self, persons):
        def convert(person):
            return Person(person_id=str(person.id),
                          firstname=person.firstname,
                          lastname=person.lastname)
        return list(map(convert, persons))

    @db_session   # или в начале функции with db_session:
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    @db_session   # или в начале функции with db_session:
    def get_person_list(self):
        return self.convert_persons_to_model(select(p for p in ORMFixture.ORMPerson if p.deprecated is None))

    @db_session
    def get_persons_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_persons_to_model(orm_group.persons)

    @db_session
    def get_persons_not_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_persons_to_model(
            select(p for p in ORMFixture.ORMPerson if p.deprecated is None and orm_group not in p.groups))

    @db_session
    def get_group_in_person(self, person):
        orm_person = list(select(p for p in ORMFixture.ORMPerson if p.id == person.person_id))[0]
        return self.convert_groups_to_model(
            select(g for g in ORMFixture.ORMGroup if orm_person in g.persons))
