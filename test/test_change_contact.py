
from model.contact import Contact
from random import randrange


def test_add_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="test"))
    old_contact = app.contact.get_contact_list()
    index = randrange(len(old_contact))
    contact = Contact(firstname="jjjj", middlename="jjj", lastname="jjjj",
                            nickname="dsbsbdds", title="sdbdsbbd")
    contact.id = old_contact[index].id
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contact) == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact[index] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)