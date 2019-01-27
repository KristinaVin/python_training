from model.group import Group


def test_change_first_group(app):
    app.group.change_first_group(Group(name="fff", header="ffff", footer="ffff"))
