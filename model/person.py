# -*- coding: utf-8 -*-

from sys import maxsize


class Person:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None,
                 address=None, home=None, mobile=None, work=None, fax=None, email=None, email2=None, email3=None,
                 homepage=None, bday=None, bmonth=None, byear=None, aday=None, amonth=None, ayear=None, address2=None,
                 phone2=None, notes=None, person_id=None, all_phones_from_homepage=None, all_emails_from_homepage=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday= aday
        self.amonth = amonth
        self.ayear = ayear
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.person_id = person_id
        self.all_phones_from_homepage = all_phones_from_homepage
        self.all_emails_from_homepage = all_emails_from_homepage

    def __repr__(self):
        return "{}:{}:{}".format(self.person_id, self.firstname, self.lastname)

    def __eq__(self, other):
        return ((self.person_id is None or other.person_id is None or self.person_id == other.person_id)
                and self.firstname == other.firstname
                and self.lastname == other.lastname)

    def id_or_max(self):
        if self.person_id:
            return int(self.person_id)
        else:
            return maxsize

    def get_data_as_string_for_log(self):
        return ("firstname: {} \n"
                "middlename: {}\n"
                "lastname: {} \n"
                "nickname: {} \n"
                "title: {} \n"
                "company: {}\n"
                "address: {}\n"
                "home: {}\n"
                "mobile: {}\n"
                "work: {}\n"
                "fax: {}\n"
                "email: {}\n"
                "email2: {}\n"
                "email3: {}\n"
                "homepage: {}\n"
                "bday: {}\n"
                "bmonth: {}\n"
                "byear: {}\n"
                "aday: {}\n"
                "amonth: {}\n"
                "ayear: {}\n"
                "address2: {}\n"
                "phone2: {}\n"
                "notes: {}\n"
                "person_id: {}\n"
                ).format(self.firstname, self.middlename, self.lastname, self.nickname, self.title,
                         self.company, self.address, self.home, self.mobile, self.work, self.fax,
                         self.email, self.email2, self.email3, self.homepage, self.bday, self.bmonth,
                         self.byear, self.aday, self.amonth, self.ayear, self.address2, self.phone2, self.notes,
                         self.person_id)

    def edit(self, new_person_data):
        self.firstname = new_person_data.firstname if new_person_data.firstname is not None else self.firstname
        self.middlename = new_person_data.middlename if new_person_data.middlename is not None else self.middlename
        self.lastname = new_person_data.lastname if new_person_data.lastname is not None else self.lastname
        self.nickname = new_person_data.nickname if new_person_data.nickname is not None else self.nickname
        self.title = new_person_data.title if new_person_data.title is not None else self.title
        self.company = new_person_data.company if new_person_data.company is not None else self.company
        self.address = new_person_data.address if new_person_data.address is not None else self.address
        self.home = new_person_data.home if new_person_data.home is not None else self.home
        self.mobile = new_person_data.mobile if new_person_data.mobile is not None else self.mobile
        self.work = new_person_data.work if new_person_data.work is not None else self.work
        self.fax = new_person_data.fax if new_person_data.fax is not None else self.fax
        self.email = new_person_data.email if new_person_data.email is not None else self.email
        self.email2 = new_person_data.email2 if new_person_data.email2 is not None else self.email2
        self.email3 = new_person_data.email3 if new_person_data.email3 is not None else self.email3
        self.homepage = new_person_data.homepage if new_person_data.homepage is not None else self.homepage
        self.bday = new_person_data.bday if new_person_data.bday is not None else self.bday
        self.bmonth = new_person_data.bmonth if new_person_data.bmonth is not None else self.bmonth
        self.byear = new_person_data.byear if new_person_data.byear is not None else self.byear
        self.aday = new_person_data.aday if new_person_data.aday is not None else self.aday
        self.amonth = new_person_data.amonth if new_person_data.amonth is not None else self.amonth
        self.ayear = new_person_data.ayear if new_person_data.ayear is not None else self.ayear
        self.address2 = new_person_data.address2 if new_person_data.address2 is not None else self.address2
        self.phone2 = new_person_data.phone2 if new_person_data.phone2 is not None else self.phone2
        self.notes = new_person_data.notes if new_person_data.notes is not None else self.notes
