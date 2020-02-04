# -*- coding: utf-8 -*-

from model.group import Group


def checking_preconditions_before_edit(app):
    if app.group.count() == 0:
        app.group.create(Group(name='for_edit'))


def test_edit_first_group_name(app):
    checking_preconditions_before_edit(app)
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(name="edited_name"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


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
