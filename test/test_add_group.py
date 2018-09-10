# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="nazwa_grupy", header="header_grupy", footer="footer_grupy"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
