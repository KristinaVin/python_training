from selenium import webdriver
from fixture.contact import ContactHelper



class Сontact_fixture:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.contact = ContactHelper(self)




    def logout(self):
        driver = self.driver
        driver.find_element_by_link_text("Logout").click()

    def return_to_home_page(self):
        driver = self.driver
        driver.find_element_by_link_text("home").click()

    def login(self, login, password):
        driver = self.driver
        self.open_home_page()
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(login)
        driver.find_element_by_name("pass").click()
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/")

    def destroy(self):
        self.driver.quit()

