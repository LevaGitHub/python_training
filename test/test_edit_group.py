# -*- coding: utf-8 -*-

from model.group import Group
import random


def checking_preconditions_before_edit(app):
    if app.group.count() == 0:
        app.group.create(Group(name='for_edit'))


def test_edit_first_group_name(app, db, check_ui):
    checking_preconditions_before_edit(app)
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    edited_group = Group(name="edited_name")
    edited_group.id = group.id
    app.group.edit_group_by_id(edited_group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups.remove(group)
    group.edit(edited_group)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
