# -*- coding: utf-8 -*-

from model.group import Group


def checking_preconditions_before_delete(app):
    if app.group.count() == 0:
        app.group.create(Group(name='for_delete'))


def test_delete_first_group(app):
    checking_preconditions_before_delete(app)
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
