from fixture.contact import ContactHelper
from fixture.session import SessionHelper
from fixture.group import GroupHelper

class Manager:



    def __init__(self):
        self.contact = ContactHelper(self)
        self.session = SessionHelper (self)
        self.group = GroupHelper (self)

