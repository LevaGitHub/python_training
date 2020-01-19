# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
import string
import random
from group import Group
from person import Person
from application import Application

days = [i for i in range(1, 32)]
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
          "December"]
years = [i for i in range(1970, 2000)]

def generate_chars_sequence(size, seq):
    return ''.join(random.choice(seq) for _ in range(size))


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    def test_add_group(self):
        self.app.login(username="admin", password="secret")
        self.app.create_group(Group(name="name", header="group header", footer="group footer"))
        self.app.return_to_groups_page()
        self.app.logout()

    def test_add_empty_group(self):
        self.app.login(username="admin", password="secret")
        self.app.create_group(Group(name="", header="", footer=""))
        self.app.return_to_groups_page()
        self.app.logout()

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def tearDown(self):
        self.app.destroy()

    def test_add_person(self):
        self.app.login(username="admin", password="secret")
        self.app.open_person()
        pers = Person(firstname=generate_chars_sequence(20, string.ascii_letters),
                      middlename=generate_chars_sequence(20, string.ascii_letters),
                      lastname=generate_chars_sequence(20, string.ascii_letters),
                      nickname=generate_chars_sequence(20, string.ascii_letters),
                      title=generate_chars_sequence(20, string.ascii_letters),
                      company=generate_chars_sequence(20, string.ascii_letters),
                      address=generate_chars_sequence(20, string.ascii_letters),
                      home=generate_chars_sequence(2, string.digits),
                      mobile=generate_chars_sequence(11, string.digits),
                      work=generate_chars_sequence(20, string.ascii_letters),
                      fax=generate_chars_sequence(11, string.digits),
                      email=generate_chars_sequence(20, string.ascii_letters),
                      email2=generate_chars_sequence(20, string.ascii_letters),
                      email3=generate_chars_sequence(20, string.ascii_letters),
                      homepage=generate_chars_sequence(20, string.ascii_letters),
                      bday=random.choice(days),
                      bmonth=random.choice(months),
                      byear=random.choice(years),
                      aday=random.choice(days),
                      amonth=random.choice(months),
                      ayear=random.choice(years),
                      address2=generate_chars_sequence(20, string.ascii_letters),
                      phone2=generate_chars_sequence(11, string.digits),
                      notes=generate_chars_sequence(50, string.ascii_letters))
        self.app.input_person_data(pers)
        self.app.return_to_home_page()
        self.app.logout()

if __name__ == "__main__":
    unittest.main()
