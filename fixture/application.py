from selenium import webdriver
from fixture.contact import ContactHelper
from fixture.session import SessionHelper
from fixture.group import GroupHelper


class Application:


    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(2)
        self.contact = ContactHelper(self)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()

    def return_to_home_page(self):
        wd = self.wd
        if not len(wd.find_elements_by_name("add")) > 0:
            wd.find_element_by_link_text("home").click()


    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False