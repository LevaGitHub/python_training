# -*- coding: utf-8 -*-

from model.person import Person


def get_edit_button_name(index):
    if index == 0:
        return "// img[ @ alt = 'Edit']"
    else:
        return "(// img[ @ alt = 'Edit'])[{}]".format(index+1)


class PersonHelper:

    def __init__(self, app):
        self.app = app

    def open_add_person_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def open_all_person_page(self):
        wd = self.app.wd
        # открываем форму если url не заканчивается на 'addressbook/' и
        # количество уникальных для формы "home" элементов = 0, значит мы не на главной сранице
        if wd.current_url[-12:] != 'addressbook/' and len(wd.find_elements_by_xpath('//*[@id="maintable"]')) == 0:
            wd.find_element_by_link_text("home").click()

    def create(self, person):
        wd = self.app.wd
        self.open_add_person_page()
        self.input_person_data(person)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_home_page()
        self.person_cache = None

    def input_person_data(self, pers):
        self.app.set_textbox_value("firstname", pers.firstname)
        self.app.set_textbox_value("middlename", pers.middlename)
        self.app.set_textbox_value("lastname", pers.lastname)
        self.app.set_textbox_value("nickname", pers.nickname)
        self.app.set_textbox_value("title", pers.title)
        self.app.set_textbox_value("company", pers.company)
        self.app.set_textbox_value("address", pers.address)
        self.app.set_textbox_value("home", pers.home)
        self.app.set_textbox_value("mobile", pers.mobile)
        self.app.set_textbox_value("work", pers.work)
        self.app.set_textbox_value("fax", pers.fax)
        self.app.set_textbox_value("email", pers.email)
        self.app.set_textbox_value("email2", pers.email2)
        self.app.set_textbox_value("email3", pers.email3)
        self.app.set_textbox_value("homepage", pers.homepage)
        self.app.select_combobox_value("bday", "%s" % pers.bday)
        self.app.select_combobox_value("bmonth", "%s" % pers.bmonth)
        self.app.set_textbox_value("byear", pers.byear)
        self.app.select_combobox_value("aday", "%s" % pers.aday)
        self.app.select_combobox_value("amonth", "%s" % pers.amonth)
        self.app.set_textbox_value("ayear", pers.ayear)
        self.app.set_textbox_value("address2", pers.address2)
        self.app.set_textbox_value("phone2", pers.phone2)
        self.app.set_textbox_value("notes", pers.notes)

    def delete_person_by_index(self, index):
        wd = self.app.wd
        self.open_all_person_page()
        self.select_person_by_index(index)
        wd.find_element_by_xpath("(//input[@name='update'])[3]").click()
        self.open_all_person_page()
        self.person_cache = None

    def select_person_by_index(self, index):
        wd = self.app.wd
        wd.find_element_by_xpath(get_edit_button_name(index)).click()

    def edit_person_by_index(self, index, edited_person):
        wd = self.app.wd
        self.open_all_person_page()
        self.select_person_by_index(index)
        self.input_person_data(edited_person)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.open_all_person_page()
        self.person_cache = None

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def count(self):
        wd = self.app.wd
        self.open_all_person_page()
        return len(wd.find_elements_by_name("selected[]"))

    person_cache = None

    def get_person_list(self):
        if self.person_cache is None:
            wd = self.app.wd
            self.open_all_person_page()
            self.person_cache = []
            rows = wd.find_elements_by_name("entry")
            for each in rows:
                columns = each.find_elements_by_css_selector("td")
                column_id = columns[0]
                person_id = column_id.find_element_by_name('selected[]').get_attribute("value")
                column_lastname = columns[1]
                lastname = column_lastname.text
                column_firstname = columns[2]
                firstname = column_firstname.text
                self.person_cache.append(Person(firstname=firstname, lastname=lastname, person_id=person_id))
        return self.person_cache

