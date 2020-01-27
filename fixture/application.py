from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.person import PersonHelper

waiting_time = 5


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(waiting_time)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.person = PersonHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get("https://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()

    def set_textbox_value(self, textbox_name, value):
        wd = self.wd
        if value is not None:
            wd.find_element_by_name(textbox_name).click()
            wd.find_element_by_name(textbox_name).clear()
            wd.find_element_by_name(textbox_name).send_keys(value)

    def select_combobox_value(self, combobox_name, value):
        wd = self.wd
        if value is not None:
            wd.find_element_by_name(combobox_name).click()
            wd.find_element_by_name(combobox_name).send_keys(value)
