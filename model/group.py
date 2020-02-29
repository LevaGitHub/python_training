# -*- coding: utf-8 -*-
from sys import maxsize


class Group:

    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    def __repr__(self):
        return "%s %s %s %s" % (self.id, self.name, self.header, self.footer)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    def edit(self, new_group_data):
        self.name = new_group_data.name if new_group_data.name is not None else self.name
        self.header = new_group_data.header if new_group_data.header is not None else self.header
        self.footer = new_group_data.footer if new_group_data.footer is not None else self.footer
        self.id = new_group_data.id if new_group_data.id is not None else self.id
