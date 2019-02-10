from model.group import Group
from random import randrange
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [
    Group(name=name, header=header, footer=footer)
    for name in ["", random_string("name",10)]
    for header in ["", random_string("header",20)]
    for footer in ["", random_string("footer",20)]
]

@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_delete_some_group(app, group):
    if app.group.count() == 0:
        app.group.create(group)
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index)
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index:index + 1] = []
    assert old_groups == new_groups