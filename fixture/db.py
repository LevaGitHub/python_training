import pymysql
from model.group import Group
from model.person import Person


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        l = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                l.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return l

    def get_person_list(self):
        print("Выполняется получение списка контактов из БД")
        l = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname) = row
                l.append(Person(person_id=str(id), firstname=firstname, lastname=lastname))
        finally:
            cursor.close()
        return l

    def destroy(self):
        self.connection.close()
