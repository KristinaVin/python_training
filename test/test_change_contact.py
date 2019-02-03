
from model.contact import Contact


def test_add_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="test"))
    old_contact = app.contact.get_contact_list()
    contact = Contact(firstname="jjjj", middlename="jjj", lastname="jjjj",
                            nickname="dsbsbdds", title="sdbdsbbd")
    contact.id = old_contact[0].id
    app.contact.change_first_contact(contact)
    assert len(old_contact)  == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact[0] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)