from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        self.input_group_data(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def open_groups_page(self):
        wd = self.app.wd
        if not(wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def edit_first_group(self, edited_group):
        wd = self.app.wd
        self.open_groups_page()
        # select first group
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("edit").click()
        self.input_group_data(edited_group)
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        # select first group
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def input_group_data(self, group):
        self.app.set_textbox_value("group_name", group.name)
        self.app.set_textbox_value("group_header", group.header)
        self.app.set_textbox_value("group_footer", group.footer)

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_group_list(self):
        wd = self.app.wd
        self.open_groups_page()
        groups = []
        for each in wd.find_elements_by_css_selector("span.group"):
            group_name = each.text
            group_id = each.find_element_by_name("selected[]").get_attribute("value")
            groups.append(Group(name=group_name, id=group_id))
        return groups
