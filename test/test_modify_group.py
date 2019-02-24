from model.group import Group
import random



def test_modify_group_name(app, db, json_groups, check_ui):
    group = json_groups
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='test'))
    old_groups = db.get_group_list()
    group_to_modify = random.choice(old_groups)
    group.id = group_to_modify.id
    app.group.modify_group_by_id(group_to_modify.id, group)
    new_groups = db.get_group_list()
    old_groups.remove(group_to_modify)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

