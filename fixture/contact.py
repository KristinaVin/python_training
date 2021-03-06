from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re

class ContactHelper:

    def __init__(self, app):
        self.app = app


    def delete_contact_homepage(self):
        wd = self.app.wd
        self.delete_contact_homepage_by_index(0)

    def delete_contact_homepage_by_index(self, index):
        wd = self.app.wd
        self.app.return_to_home_page()
        #  select first contact
        self.select_contact_by_index(index)
        #  submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_elements_by_css_selector("div.msgbox")
        self.app.return_to_home_page()
        self.contact_cache = None


    def delete_first_contact(self):
        wd = self.app.wd
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.return_to_home_page()
        #  select first contact
        self.choice_del_contact_by_index(index)
        #  submit deletion
        wd.find_element_by_xpath("(//input[@name='update'])[3]").click()
        wd.find_elements_by_css_selector("div.msgbox")
        self.app.return_to_home_page()
        self.contact_cache = None



    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.app.return_to_home_page()
        #  select first contact
        self.choice_del_contact_by_id(id)
        #  submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.app.return_to_home_page()
        self.contact_cache = None

    def choice_del_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def choice_del_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def change_first_contact(self):
        wd = self.app.wd
        self.modify_contact_by_index(0)

    def  modify_contact_by_index(self, index, contact):
        self.app.return_to_home_page()
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        #  submit modification
        self.contract_form_fill(contact)
        wd.find_element_by_name("update").click()
        self.app.return_to_home_page()
        self.contact_cache = None


    def  modify_contact_by_id(self, id, contact):
        self.app.return_to_home_page()
        wd = self.app.wd
        self.open_contact_to_edit_by_id(id)
        #  submit modification
        self.contract_form_fill(contact)
        wd.find_element_by_name("update").click()
        self.app.return_to_home_page()
        self.contact_cache = None


    def open_contact_view_by_index (self,index):
        wd = self.app.wd
        self.app.open_home_page()
        row= wd.find_elements_by_name("entry")[index]
        cell=row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()


    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_to_edit_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        self.app.open_home_page()
        wd.find_element_by_xpath("//input[@value='{0}']//..//..//td[8]//a".format(id)).click()

    def select_first_contact(self):
        wd = self.app.wd
        self.select_contact_by_index(0)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_form_value(self, form_name, text, xpath):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(form_name).click()
            Select(wd.find_element_by_name(form_name)).select_by_visible_text(text)
            wd.find_element_by_xpath(xpath).click()



    def contract_form_fill(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        # input_contact_telephones
        self.change_field_value("home", contact.home_telephone)
        self.change_field_value("mobile", contact.mobile_telephone)
        self.change_field_value("work", contact.work_telephone)
        self.change_field_value("fax", contact.fax)
        # input_contact_emails
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        # input_contact_homepage
        self.change_field_value("homepage", contact.homepage)
        # input_contact_birthday
        self.change_form_value("bday",contact.bday, "//option[@value='10']")
        self.change_form_value("bmonth", contact.bmonth, "//option[@value='November']")
        self.change_field_value("byear", contact.byear)
        self.change_form_value("aday", contact.aday, "(//option[@value='12'])[2]")
        self.change_form_value("amonth", contact.amonth, "(//option[@value='October'])[2]")
        self.change_field_value("ayear", contact.ayear)
        # input_contact_Secondary_information
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)



    def create_contact(self, contact):
        wd = self.app.wd
        self.app.return_to_home_page()
        self.open_add_new_page()
        self.contract_form_fill(contact)
        # submit_contact_creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.app.return_to_home_page()
        self.contact_cache = None

    def open_add_new_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("submit")) > 0):
            wd.find_element_by_link_text("add new").click()

    def count(self):
        wd = self.app.wd
        self.app.return_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.app.return_to_home_page()
        self.open_add_new_page()
        self.select_first_contact()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.contract_form_fill(new_contact_data)
        wd.find_element_by_name("update").click()
        self.app.return_to_home_page()
        self.contact_cache = None

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                firstname = cells[2].text
                lastname = cells[1].text
                address = cells[3].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text
                all_emails = cells[4].text
                self.contact_cache.append(Contact(firstname=firstname, lastname = lastname, id=id, address=address,
                                                  all_phones_from_home_page = all_phones, all_emails_from_homepage = all_emails ))
        return list(self.contact_cache)



    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home_telephone = wd.find_element_by_name("home").get_attribute("value")
        work_telephone = wd.find_element_by_name("work").get_attribute("value")
        mobile_telephone = wd.find_element_by_name("mobile").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       home_telephone=home_telephone, work_telephone=work_telephone,
                       mobile_telephone=mobile_telephone, phone2=phone2,
                       email=email, email2=email2, email3=email3, address=address)


    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home_telephone = re.search("H: (.*)", text).group(1)
        work_telephone = re.search("W: (.*)", text).group(1)
        mobile_telephone = re.search("M: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(home_telephone=home_telephone, work_telephone=work_telephone,
                       mobile_telephone=mobile_telephone, phone2=phone2)

    def add_contact_to_group(self, Contact, Group):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(Contact.id)
        wd.find_element_by_name("to_group").send_keys(Group.name)
        wd.find_element_by_name("add").click()

    def delete_contact_from_group(self, Contact, Group):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("group").send_keys(Group.name)
        wd.find_element_by_css_selector("body").click()
        self.select_contact_by_id(Contact.id)
        wd.find_element_by_name("remove").click()
        self.app.return_to_home_page()
        wd.find_element_by_name("group").send_keys("[all]")
        wd.find_element_by_css_selector("body").click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()