# -*- coding: utf-8 -*-

from model.group import Group


def checking_preconditions_before_delete(app):
    if app.group.count() == 0:
        app.group.create(Group(name='for_delete'))


def test_delete_first_group(app):
    checking_preconditions_before_delete(app)
    app.group.delete_first_group()
