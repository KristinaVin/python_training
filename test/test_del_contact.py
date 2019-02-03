from model.contact import Contact

def test_del_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="dsbsbdsb", middlename="sdbdbsdbs", lastname="sdbsddbs",
                            nickname="dsbsbdds", title="sdbdsbbd", company="dsbsdbsb", address="sbsbsbdbd",
                            home_telephone="7216412546", mobile_telephone="7214651645", work_telephone="762145164", fax="ksskakk",
                            email="lalasla@mail.ru", email2="jwfkqjfkqjwfl@mail.ru", email3="qfw@mail.ru",
                            homepage="dbbdddbbb", bday="10", bmonth="November", byear="1990",aday="12", amonth="October",
                            ayear="1999", notes="dvdvssdvd", address2="dvdsdsv", phone2="vsdsvdsvd"))
    old_contact = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    assert len(old_contact) - 1 == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact[0:1] = []
    assert old_contact == new_contact