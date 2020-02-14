# -*- coding: utf-8 -*-

from model.group import Group
from fixture.general import generate_sequence
import pytest
import random
import string

test_seq = string.ascii_letters + string.digits + string.punctuation + " " * 10

test_data = [
    Group(name=name, header=header, footer=footer)
    for name in ["", generate_sequence(random.randrange(10), test_seq, prefix='name')]
    for header in ["", generate_sequence(random.randrange(20), test_seq, prefix='header')]
    for footer in ["", generate_sequence(random.randrange(30), test_seq, prefix='footer')]
]


@pytest.mark.parametrize("group", test_data, ids=[str(x) for x in test_data])
def test_add_group(app, group):
    pass
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

