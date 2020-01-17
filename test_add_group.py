# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
import string
import random
from group import Group
from person import Person

days = [i for i in range(1, 32)]
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
          "December"]
years = [i for i in range(1970, 2000)]


def generate_chars_sequence(size, seq):
    return ''.join(random.choice(seq) for _ in range(size))


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_groups_page(wd)
        self.create_group(wd, Group(name="name", header="group header", footer="group footer"))
        self.return_to_groups_page(wd)
        self.logout(wd)

    def test_add_empty_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_groups_page(wd)
        self.create_group(wd, Group(name="", header="", footer=""))
        self.return_to_groups_page(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_to_groups_page(self, wd):
        wd.find_element_by_link_text("group page").click()

    def create_group(self, wd, group):
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()

    def open_groups_page(self, wd):
        wd.find_element_by_link_text("groups").click()

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("https://localhost/addressbook/")

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
        self.wd.quit()

    def test_add_person(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_person(wd)
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
        self.input_person_data(wd, pers)
        self.return_to_home_page(wd)
        self.logout(wd)

    def return_to_home_page(self, wd):
        wd.find_element_by_link_text("home page").click()

    def input_person_data(self, wd, pers):
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(pers.firstname)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(pers.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(pers.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(pers.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(pers.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(pers.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(pers.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(pers.home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(pers.mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(pers.work)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(pers.fax)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(pers.email)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(pers.email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(pers.email3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(pers.homepage)
        wd.find_element_by_name("bday").click()
        wd.find_element_by_name("bday").send_keys("%s" % pers.bday)
        wd.find_element_by_name("bmonth").click()
        wd.find_element_by_name("bmonth").send_keys("%s" % pers.bmonth)
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(pers.byear)
        wd.find_element_by_name("aday").click()
        wd.find_element_by_name("aday").click()
        wd.find_element_by_name("aday").send_keys("%s" % pers.aday)
        wd.find_element_by_name("amonth").click()
        wd.find_element_by_name("amonth").send_keys("%s" % pers.amonth)
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(pers.ayear)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(pers.address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(pers.phone2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(pers.notes)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def open_person(self, wd):
        wd.find_element_by_link_text("add new").click()


if __name__ == "__main__":
    unittest.main()
