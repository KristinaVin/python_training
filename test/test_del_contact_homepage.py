from model.contact import Contact


def test_del_contact(app):
    if app.contact.count == 0:
        app.contact.create(Contact(name="test"))
    app.contact.delete_contact_homepage()
