from model.contact import Contact
from random import randrange



def test_del_contact(app,json_contacts):
    contact=json_contacts
    if app.contact.count() == 0:
        app.contact.create_contact(contact)
    old_contact = app.contact.get_contact_list()
    index = randrange(len(old_contact))
    app.contact.delete_contact_by_index(index)
    assert len(old_contact) - 1 == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact[index:index + 1] = []
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)

