import pymysql.cursors
from fixture.orm import ORMFixture
from model.group import Group

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    '''
    groups = db.get_group_list()
    for group in groups:
        print(group)
    print(len(groups))

    persons = db.get_person_list()
    for person in persons:
        print(person)
    print(len(persons))

    l = db.get_person_list()
    '''
    l = db.get_persons_not_in_group(Group(id="120"))
    for each in l:
        print(each)
    print(len(l))
finally:
    pass   # db.destroy()
