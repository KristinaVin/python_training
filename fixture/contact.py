from selenium.webdriver.support.ui import Select
from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def delete_contact_homepage(self):
        wd = self.app.wd
        self.app.return_to_home_page()
        #  select first contact
        wd.find_element_by_name("selected[]").click()
        #  submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.app.return_to_home_page()



    def delete_first_contact(self):
        wd = self.app.wd
        self.app.return_to_home_page()
        #  select first contact
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        #  submit deletion
        wd.find_element_by_xpath("(//input[@name='update'])[3]").click()
        self.app.return_to_home_page()

    def change_first_contact(self, contact):
        self.app.return_to_home_page()
        wd = self.app.wd
        self.select_first_contact()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        #  submit modification
        self.contract_form_fill(contact)
        wd.find_element_by_name("update").click()
        self.app.return_to_home_page()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

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

    def get_contact_list(self):
        wd = self.app.wd
        contacts = []
        for element in wd.find_elements_by_css_selector("tr")[1:]:
            text = element.find_element_by_name("selected[]").get_attribute("title")
            id = element.find_element_by_name("selected[]").get_attribute("id")
            contacts.append(Contact(firstname=text.split()[1][1:], lastname=text.split()[2][:-1], id=id))
        return contacts


