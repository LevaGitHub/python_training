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
        print("Выполняется получение списка групп из БД")
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

    def get_person(self, person_id):
        cursor = self.connection.cursor()
        pers_data_from_db = None
        try:
            cursor.execute("select id, firstname, lastname, address, email, email2, email3, home, mobile, work, phone2"
                           " from addressbook where (deprecated='0000-00-00 00:00:00' and id={})".format(person_id))
            for row in cursor:
                (id, firstname, lastname, address, email, email2, email3, home, mobile, work, phone2) = row
                pers_data_from_db = (Person(person_id=str(id), firstname=firstname, lastname=lastname, address=address,
                                            email=email, email2=email2, email3=email3, home=home, mobile=mobile,
                                            work=work, phone2=phone2))
        finally:
            cursor.close()
        if pers_data_from_db is None:
            raise ValueError("Unrecognize person id - %s" % person_id)
        return pers_data_from_db

    def destroy(self):
        self.connection.close()
