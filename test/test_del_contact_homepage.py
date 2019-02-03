from model.contact import Contact
from random import randrange


def test_del_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="dsbsbdsb", middlename="sdbdbsdbs", lastname="sdbsddbs",
                            nickname="dsbsbdds", title="sdbdsbbd", company="dsbsdbsb", address="sbsbsbdbd",
                            home_telephone="7216412546", mobile_telephone="7214651645", work_telephone="762145164", fax="ksskakk",
                            email="lalasla@mail.ru", email2="jwfkqjfkqjwfl@mail.ru", email3="qfw@mail.ru",
                            homepage="dbbdddbbb", bday="10", bmonth="November", byear="1990",aday="12", amonth="October",
                            ayear="1999", notes="dvdvssdvd", address2="dvdsdsv", phone2="vsdsvdsvd"))
    old_contact = app.contact.get_contact_list()
    index = randrange(len(old_contact))
    app.contact.delete_contact_homepage_by_index(index)
    assert len(old_contact) - 1 == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact[index:index + 1] = []
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)