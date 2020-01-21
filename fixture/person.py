class PersonHelper:

    def __init__(self, app):
        self.app = app

    def open_add_person_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def open_all_person_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def create(self, person):
        wd = self.app.wd
        self.open_add_person_page()
        self.input_person_data(person)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_home_page()

    def input_person_data(self, pers):
        wd = self.app.wd
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

    def delete_first_person(self):
        wd = self.app.wd
        self.open_all_person_page()
        wd.find_element_by_xpath("(//img[@alt='Edit'])[2]").click()
        wd.find_element_by_xpath("(//input[@name='update'])[3]").click()
        self.open_all_person_page()

    def edit_first_person(self, edited_person):
        wd = self.app.wd
        self.open_all_person_page()
        wd.find_element_by_xpath("(//img[@alt='Edit'])[2]").click()
        self.input_person_data(edited_person)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.open_all_person_page()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()
