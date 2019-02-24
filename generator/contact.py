from model.contact import Contact
import random
import string
import jsonpickle
import os.path
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 2
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


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
            for i in range(2)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
