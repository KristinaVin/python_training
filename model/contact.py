from sys import maxsize

class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None, address=None,
                 all_phones_from_home_page = None, all_emails_from_homepage = None,
                 home_telephone=None,
                       mobile_telephone=None, work_telephone=None, fax=None, email=None, email2=None, email3=None,  homepage=None, bday=None, bmonth=None, byear=None, aday=None, amonth=None, ayear=None, notes=None,
                       address2=None, phone2=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home_telephone = home_telephone
        self.mobile_telephone = mobile_telephone
        self.work_telephone = work_telephone
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.notes = notes
        self.address2 = address2
        self.phone2 = phone2
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_homepage = all_emails_from_homepage

    def __repr__(self):
        return "%s:%s:%s:%s:(%s:%s:%s):{%s:%s:%s:%s}" % (self.id, self.lastname, self.firstname, self.address,
                                                         self.email, self.email2, self.email3, self.home_telephone,
                                                         self.mobile_telephone, self.work_telephone, self.phone2)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and (self.firstname is None or other.firstname is None or self.firstname == other.firstname) \
               and (self.lastname is None or other.lastname is None or self.lastname == other.lastname)





    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize