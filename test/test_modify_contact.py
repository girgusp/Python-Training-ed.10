def test_modify_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify()
    app.session.logout()