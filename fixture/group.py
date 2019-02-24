from model.group import Group
from model.contact import Contact
from random import randrange
import random

class GroupHelper:

    contact_cache = None

    def __init__(self, app):
        self.app = app

    def return_to_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_link_text("group page")) > 0):
            wd.find_element_by_link_text("group page").click()

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()
        wd.find_element_by_link_text("home").click()
        self.group_cache = None

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        wd.find_element_by_link_text("home").click()
        self.group_cache = None

    def delete_group_by_id(self, id):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(id)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        wd.find_element_by_link_text("home").click()
        self.group_cache = None

    def select_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()


    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()


    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def modify_first_group(self):
        wd = self.app.wd
        self.modify_group_by_index(0)

    def modify_group_by_index(self, index, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        # open modification form
        wd.find_element_by_name("edit").click()
        # fill group form
        self.fill_group_form (new_group_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cache = None


    def  modify_group_by_id(self, id, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(id)
        # open modification form
        wd.find_element_by_name("edit").click()
        # fill group form
        self.fill_group_form (new_group_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector ("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def find_group_to_add_contact(self, Contact):
        wd = self.app.wd
        self.return_to_home_page()
        groups = self.get_group_list()
        self.return_to_home_page()
        while 1:
            group = random.choice(groups)
            wd.find_element_by_name("group").send_keys(group.name)
            wd.find_element_by_css_selector("body").click()
            contacts = self.get_contact_list_in_group()
            if Contact not in contacts:
                wd.find_element_by_name("group").send_keys("[all]")
                wd.find_element_by_css_selector("body").click()
                return group, contacts

    def group_contacts(self, Group):
        wd = self.app.wd
        self.return_to_home_page()
        wd.find_element_by_name("group").send_keys(Group.name)
        wd.find_element_by_css_selector("body").click()
        contacts = self.get_contact_list_in_group()
        wd.find_element_by_name("group").send_keys("[all]")
        wd.find_element_by_css_selector("body").click()
        return contacts

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page(wd)
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                address = cells[3].text
                first_name = cells[2].text
                last_name = cells[1].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text
                all_emails = cells[4].text
                self.contact_cache.append(Contact(firstname=first_name, lastname=last_name, id=id, address=address,
                                                  all_phones_from_home_page=all_phones,
                                                  all_emails_from_homepage=all_emails))
        return list(self.contact_cache)

    def get_contact_list_in_group(self):
        wd = self.app.wd
        self.contact_cache = []
        for row in wd.find_elements_by_name("entry"):
            cells = row.find_elements_by_tag_name("td")
            address = cells[3].text
            first_name = cells[2].text
            last_name = cells[1].text
            id = cells[0].find_element_by_tag_name("input").get_attribute("value")
            all_phones = cells[5].text
            all_emails = cells[4].text
            self.contact_cache.append(Contact(firstname=first_name, lastname=last_name, id=id, address=address,
                                              all_phones_from_home_page=all_phones,
                                              all_emails_from_homepage=all_emails))
        return list(self.contact_cache)