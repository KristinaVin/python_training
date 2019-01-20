# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.contact_fixture import Сontact_fixture



@pytest.fixture
def con_fix(request):
    fixture = Сontact_fixture()
    request.addfinalizer(fixture.destroy)
    return fixture



def test_add_contact(con_fix):
    con_fix.login(login="admin", password="secret")
    con_fix.contact.create_contact(Contact(firstname="dsbsbdsb", middlename="sdbdbsdbs", lastname="sdbsddbs",
                            nickname="dsbsbdds", title="sdbdsbbd", company="dsbsdbsb", address="sbsbsbdbd",
                            home_telephone="7216412546", mobile_telephone="7214651645", work_telephone="762145164", fax="ksskakk",
                            email="lalasla@mail.ru", email2="jwfkqjfkqjwfl@mail.ru", email3="qfw@mail.ru",
                            homepage="dbbdddbbb", bday="10", bmonth="November", byear="1990",aday="12", amonth="October",
                            ayear="1999", notes="dvdvssdvd", address2="dvdsdsv", phone2="vsdsvdsvd"))
    con_fix.logout()
