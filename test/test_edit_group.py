# -*- coding: utf-8 -*-

from model.group import Group


def checking_preconditions_before_edit(app):
    if app.group.count() == 0:
        app.group.create(Group(name='for_edit'))


def test_edit_first_group_name(app):
    checking_preconditions_before_edit(app)
    app.group.edit_first_group(Group(name="edited_name"))


def test_edit_first_group_header(app):
    checking_preconditions_before_edit(app)
    app.group.edit_first_group(Group(header="edited_group_header"))


def test_edit_first_group_footer(app):
    checking_preconditions_before_edit(app)
    app.group.edit_first_group(Group(footer="edited_group_footer"))
