# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_add_contact(self):
        driver = self.driver
        self.open_home_page(driver)
        self.login(driver, login="admin", password="secret")
        self.open_add_new_page(driver)
        self.create_contact(driver, firstname="dsbsbdsb", middlename="sdbdbsdbs", lastname="sdbsddbs",
                            nickname="dsbsbdds", title="sdbdsbbd", company="dsbsdbsb", address="sbsbsbdbd",
                            home_telephone="7216412546", mobile_telephone="7214651645", work_telephone="762145164",
                            email="lalasla@mail.ru", email2="jwfkqjfkqjwfl@mail.ru", email3="qfw@mail.ru", fax="ksskakk",
                            homepage="dbbdddbbb", bday="10", bmonth="November", byear="1990",aday="12", amonth="October",
                            ayear="1999", notes="dvdvssdvd", address2="dvdsdsv", phone2="vsdsvdsvd")
        self.return_to_home_page(driver)
        self.logout(driver)

    def logout(self, driver):
        driver.find_element_by_link_text("Logout").click()

    def return_to_home_page(self, driver):
        driver.find_element_by_link_text("home").click()

    def create_contact(self, driver, firstname, middlename, lastname, nickname, title, company, address, home_telephone,
                       mobile_telephone, work_telephone, email, email2, email3, fax, homepage, bday, bmonth, byear, aday, amonth, ayear, notes,
                       address2, phone2):
        # input_contact_personal_information
        driver.find_element_by_name("firstname").click()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys(firstname)
        driver.find_element_by_name("middlename").click()
        driver.find_element_by_name("middlename").clear()
        driver.find_element_by_name("middlename").send_keys(middlename)
        driver.find_element_by_name("lastname").click()
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys(lastname)
        driver.find_element_by_name("nickname").click()
        driver.find_element_by_name("nickname").clear()
        driver.find_element_by_name("nickname").send_keys(nickname)
        driver.find_element_by_name("title").click()
        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys(title)
        driver.find_element_by_name("company").click()
        driver.find_element_by_name("company").clear()
        driver.find_element_by_name("company").send_keys(company)
        driver.find_element_by_name("address").click()
        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("address").send_keys(address)
        # input_contact_telephones
        driver.find_element_by_name("home").click()
        driver.find_element_by_name("home").clear()
        driver.find_element_by_name("home").send_keys(home_telephone)
        driver.find_element_by_name("mobile").click()
        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("mobile").send_keys(mobile_telephone)
        driver.find_element_by_name("work").click()
        driver.find_element_by_name("work").clear()
        driver.find_element_by_name("work").send_keys(work_telephone)
        driver.find_element_by_name("fax").click()
        driver.find_element_by_name("fax").clear()
        driver.find_element_by_name("fax").send_keys(fax)
        # input_contact_emails
        driver.find_element_by_name("email").click()
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys(email)
        driver.find_element_by_name("email2").click()
        driver.find_element_by_name("email2").clear()
        driver.find_element_by_name("email2").send_keys(email2)
        driver.find_element_by_name("email3").click()
        driver.find_element_by_name("email3").clear()
        driver.find_element_by_name("email3").send_keys(email3)
        # input_contact_homepage
        driver.find_element_by_name("homepage").click()
        driver.find_element_by_name("homepage").clear()
        driver.find_element_by_name("homepage").send_keys(homepage)
        # input_contact_birthday
        driver.find_element_by_name("bday").click()
        Select(driver.find_element_by_name("bday")).select_by_visible_text(bday)
        driver.find_element_by_xpath("//option[@value='10']").click()
        driver.find_element_by_name("bmonth").click()
        Select(driver.find_element_by_name("bmonth")).select_by_visible_text(bmonth)
        driver.find_element_by_xpath("//option[@value='November']").click()
        driver.find_element_by_name("byear").click()
        driver.find_element_by_name("byear").clear()
        driver.find_element_by_name("byear").send_keys(byear)
        driver.find_element_by_name("aday").click()
        Select(driver.find_element_by_name("aday")).select_by_visible_text(aday)
        driver.find_element_by_xpath("(//option[@value='12'])[2]").click()
        driver.find_element_by_name("amonth").click()
        Select(driver.find_element_by_name("amonth")).select_by_visible_text(amonth)
        driver.find_element_by_xpath("(//option[@value='October'])[2]").click()
        driver.find_element_by_name("ayear").click()
        driver.find_element_by_name("ayear").clear()
        driver.find_element_by_name("ayear").send_keys(ayear)
        # input_contact_Secondary_information
        driver.find_element_by_name("address2").click()
        driver.find_element_by_name("address2").clear()
        driver.find_element_by_name("address2").send_keys(address2)
        driver.find_element_by_name("phone2").click()
        driver.find_element_by_name("phone2").clear()
        driver.find_element_by_name("phone2").send_keys(phone2)
        driver.find_element_by_name("notes").click()
        driver.find_element_by_name("notes").clear()
        driver.find_element_by_name("notes").send_keys(notes)
        # submit_contact_creation
        driver.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def open_add_new_page(self, driver):
        driver.find_element_by_link_text("add new").click()

    def login(self, driver, login, password):
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(login)
        driver.find_element_by_name("pass").click()
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, driver):
        driver.get("http://localhost/addressbook/")

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
