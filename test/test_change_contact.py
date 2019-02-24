from model.contact import Contact
import random



def test_add_contact(app, json_contacts,  db, check_ui):
    contact = json_contacts
    if app.contact.count() == 0:
        app.contact.create(contact)
    old_contact = db.get_contact_list()
    contact_to_modify = random.choice(old_contact)
    contact.id = contact_to_modify.id
    app.contact.modify_contact_by_id(contact_to_modify.id, contact)
    new_contact = db.get_contact_list()
    old_contact.remove(contact_to_modify)
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
    if check_ui:
        assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)



