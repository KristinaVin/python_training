from model.contact import Contact
from random import randrange
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


months = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]

testdata = [
    Contact(firstname=firstname, middlename=middlename, lastname=lastname,
            nickname=nickname, title=title, company=company, address=address,
            home_telephone=home_telephone, mobile_telephone=mobile_telephone, work_telephone=work_telephone, fax=fax,
            email=email, email2=email2, email3=email3,
            homepage=homepage, bday=str(random.randrange(1, 32)), bmonth=random.choice(months), byear=random_string("byear", 10), aday=str(random.randrange(1, 32)), amonth=random.choice(months),
            ayear=random_string("a_year", 10), notes=notes, address2=address2, phone2=phone2)
    for firstname in ["", random_string("firstname",10)]
    for middlename in ["", random_string("middlename",10)]
    for lastname in ["", random_string("lastname",10)]
    for nickname in ["", random_string("nickname",10)]
    for title in ["", random_string("title",10)]
    for company in ["", random_string("company",10)]
    for address in ["", random_string("address",20)]
    for home_telephone in ["", random_string("home_telephone",6)]
    for mobile_telephone in ["", random_string("mobile_telephone",11)]
    for work_telephone in ["", random_string("work_telephone",6)]
    for fax in ["", random_string("fax", 6)]
    for email in ["", random_string("email", 15)]
    for email2 in ["", random_string("email2", 15)]
    for email3 in ["", random_string("email3", 15)]
    for homepage in ["", random_string("homepage", 20)]
    for notes in ["", random_string("notes", 25)]
    for address2 in ["", random_string("address2", 20)]
    for phone2 in ["", random_string("phone2", 15)]
]

@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_del_contact(app,contact):
    if app.contact.count() == 0:
        app.contact.create_contact(contact)
    old_contact = app.contact.get_contact_list()
    index = randrange(len(old_contact))
    app.contact.delete_contact_by_index(index)
    assert len(old_contact) - 1 == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact[index:index + 1] = []
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)

