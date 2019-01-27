
from model.contact import Contact


def test_add_contact(app):
    if app.contact.count == 0:
        app.contact.create(Contact(name="test"))
    app.contact.change_first_contact(Contact(firstname="jjjj", middlename="jjj", lastname="jjjj",
                            nickname="dsbsbdds", title="sdbdsbbd"))


