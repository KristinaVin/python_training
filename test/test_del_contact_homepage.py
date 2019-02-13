from model.contact import Contact
from random import randrange
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

months = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]

testdata = [Contact(firstname=random_string("first_name", 10), middlename=random_string("middle_name", 10),
                    lastname=random_string("last_name", 10), nickname=random_string("nickname", 10),
                     title=random_string("title", 10),
                    company=random_string("company", 10), address=random_string("address", 10),
                    home_telephone=random_string("home_phone", 10), mobile_telephone=random_string("mobile_phone", 10),
                    work_telephone=random_string("work_phone", 10), fax=random_string("fax", 10),
                    email=random_string("email_1", 10), email2=random_string("email_2", 10),
                    email3=random_string("email_3", 10), homepage=random_string("homepage", 10),
                    bday=str(random.randrange(1, 32)),  bmonth=random.choice(months), aday=str(random.randrange(1, 32)),
                    amonth=random.choice(months), byear=random_string("b_year", 10), ayear=random_string("a_year", 10),
                    address2=random_string("address_2", 10), phone2=random_string("phone_2", 10),
                    notes=random_string("notes", 10))
            for i in range(5)]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_del_contact(app, contact):
    if app.contact.count() == 0:
        app.contact.create_contact(contact)
    old_contact = app.contact.get_contact_list()
    index = randrange(len(old_contact))
    app.contact.delete_contact_homepage_by_index(index)
    assert len(old_contact) - 1 == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact[index:index + 1] = []
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)