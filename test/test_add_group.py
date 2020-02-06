# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group(app):
    added_group = Group(name="name", header="group header", footer="group footer")
    old_groups = app.group.get_group_list()
    app.group.create(added_group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(added_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

'''
def test_add_empty_group(app):
    added_group = Group(name="", header="", footer="")
    old_groups = app.group.get_group_list()
    app.group.create(added_group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(added_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
'''