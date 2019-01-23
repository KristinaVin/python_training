from selenium import webdriver
from fixture.contact import ContactHelper


class Сontact_fixture:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.contact = ContactHelper(self)



    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()
        wd.find_element_by_name("user")

    def return_to_home_page(self):
        wd = self.wd
        wd.find_element_by_link_text("home").click()

    def login(self, login, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(login)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()