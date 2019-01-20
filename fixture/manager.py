from fixture.contact import ContactHelper
from fixture.session import SessionHelper
from fixture.group import GroupHelper

class Manager:


    def __init__(self, app):
        self.app = app
        self.app.contact = ContactHelper(app)
        self.app.session = SessionHelper(app)
        self.app.group = GroupHelper(app)

