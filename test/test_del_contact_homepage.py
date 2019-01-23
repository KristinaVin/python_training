


def test_del_contact(con_fix):
    con_fix.login(login="admin", password="secret")
    con_fix.contact.delete_contact_homepage()
    con_fix.logout()