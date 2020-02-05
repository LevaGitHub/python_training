# -*- coding: utf-8 -*-

from sys import maxsize

class Person:

    def __init__(self, firstname='', middlename='', lastname='', nickname='', title='', company='', address='',
                 home='', mobile='', work='', fax='', email='', email2='', email3='', homepage='', bday='', bmonth='',
                 byear='', aday='', amonth='', ayear='', address2='', phone2='', notes='', person_id=None):
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
