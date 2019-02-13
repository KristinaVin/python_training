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
                                                         self.home_telephone, self.work_telephone, self.phone2)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and (self.firstname is None or other.firstname is None or self.firstname == other.firstname) \
               and (self.middlename is None or other.middlename is None or self.middlename == other.middlename)\
               and (self.lastname is None or other.lastname is None or self.lastname == other.lastname) \
               and (self.nickname is None or other.nickname is None or self.nickname == other.nickname) \
               and (self.title is None or other.title is None or self.title == other.title) \
               and (self.company is None or other.company is None or self.company == other.company \
               and (self.address is None or other.address is None or self.address == other.address) \
               and (self.home_telephone is None or other.home_telephone is None or self.home_telephone == other.home_telephone \
               and (self.mobile_telephone is None or other.mobile_telephone is None or self.mobile_telephone == other.mobile_telephone) \
               and (self.work_telephone is None or other.work_telephone is None or self.work_telephone == other.work_telephone) \
               and (self.fax is None or other.fax is None or self.fax == other.fax) \
               and (self.email is None or other.email is None or self.email == other.email) \
               and (self.email2 is None or other.email2 is None or self.email2 == other.email2) \
               and (self.email3 is None or other.email3 is None or self.email3 == other.email3) \
               and (self.homepage is None or other.homepage is None or self.homepage == other.homepage) \
               and (self.bday is None or other.bday is None or self.bday == other.bday) \
                    and (self.bmonth is None or other.bmonth is None or self.bmonth == other.bmonth) \
                    and (self.byear is None or other.byear is None or self.byear == other.byear) \
                    and (self.aday is None or other.aday is None or self.aday == other.aday) \
                    and (self.amonth is None or other.amonth is None or self.amonth == other.amonth) \
                    and (self.ayear is None or other.ayear is None or self.ayear == other.ayear) \
                    and (self.notes is None or other.notes is None or self.notes == other.notes) \
                    and (self.address2 is None or other.address2 is None or self.address2 == other.address2) \
                    and (self.phone2 is None or other.phone2 is None or self.phone2 == other.phone2) \
                    and (self.all_phones_from_home_page is None or other.all_phones_from_home_page is None or self.all_phones_from_home_page == other.all_phones_from_home_page) \
                    and (self.all_emails_from_homepage is None or other.all_emails_from_homepage is None or self.all_emails_from_homepage == other.all_emails_from_homepage
                         )
                    ))



    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize