# -*- coding: utf-8 -*-

from model.group import Group


def checking_preconditions_before_edit(app):
    if app.group.count() == 0:
        app.group.create(Group(name='for_edit'))


def test_edit_first_group_name(app):
    checking_preconditions_before_edit(app)
    old_groups = app.group.get_group_list()
    edited_group = Group(name="edited_name")
    edited_group.id = old_groups[0].id
    app.group.edit_first_group(edited_group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = edited_group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

'''
def test_edit_first_group_header(app):
    checking_preconditions_before_edit(app)
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(header="edited_group_header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_edit_first_group_footer(app):
    checking_preconditions_before_edit(app)
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(footer="edited_group_footer"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
'''