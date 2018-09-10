# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(first_name="FN", middle_name="MN", last_name="LN"))


def test_add_empty_contact(app):
    app.contact.create(Contact(first_name="", middle_name="", last_name=""))
