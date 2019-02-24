from model.contact import Contact
import random
from time import sleep



def test_del_contact(app, json_contacts, db, check_ui):
    add_contact=json_contacts
    if len (db.get_contact_list()) == 0:
        app.contact.create_contact(add_contact)
    old_contact = db.get_contact_list()
    contact = random.choice(old_contact)
    app.contact.delete_contact_by_id(contact.id)
    old_contact.remove(contact)
    sleep(1)
    new_contact = db.get_contact_list()
    assert old_contact == new_contact
    if check_ui:
        assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


