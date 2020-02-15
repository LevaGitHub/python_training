# -*- coding: utf-8 -*-

from model.group import Group
import fixture.general as general
import pytest

person_count = 3

test_data = [
    Group(name=general.generate_sequence(20, general.test_seq, prefix='name'),
          header=general.generate_sequence(20, general.test_seq, prefix='header'),
          footer=general.generate_sequence(20, general.test_seq, prefix='footer'))
    for _ in range(person_count)
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

