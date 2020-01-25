# -*- coding: utf-8 -*-

from model.group import Group


def test_edit_first_group_name(app):
    app.group.edit_first_group(Group(name="edited_name"))


def test_edit_first_group_header(app):
    app.group.edit_first_group(Group(header="edited_group_header"))


def test_edit_first_group_footer(app):
    app.group.edit_first_group(Group(footer="edited_group_footer"))
