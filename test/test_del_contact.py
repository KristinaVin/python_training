

def test_add_contact(con_fix):
    con_fix.login(login="admin", password="secret")
    con_fix.contact.delete_first_contact()
    con_fix.logout()