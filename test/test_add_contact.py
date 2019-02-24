# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app, db, json_contacts, check_ui):
    contact=json_contacts
    old_contact = db.get_contact_list()
    app.contact.create_contact(contact)
    new_contact = db.get_contact_list()
    old_contact.append(contact)
    assert old_contact == new_contact
    if check_ui:
        assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)