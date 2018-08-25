# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(first_name="FN", middle_name="MN", last_name="LN"))
    app.logout()


def test_add_empty_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(first_name="", middle_name="", last_name=""))
    app.logout()
