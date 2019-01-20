from model.contact import Contact


def test_add_contact(con_fix):
    con_fix.login(login="admin", password="secret")
    con_fix.contact.change_first_contact(Contact(firstname="аааа", middlename="", lastname="",
                            nickname="", title="", company="", address="",
                            home_telephone="", mobile_telephone="", work_telephone="", fax="",
                            email="", email2="", email3="",
                            homepage="", bday="", bmonth="", byear="",aday="", amonth="",
                            ayear="", notes="", address2="", phone2=""))
    con_fix.logout()