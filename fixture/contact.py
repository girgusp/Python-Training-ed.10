class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/addressbook/")

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_home_page()
        # open contacts page
        self.open_contacts_page()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_name("theform").click()
        # return to home page
        self.return_to_home_page()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.first_name)
        self.change_field_value("middlename", contact.middle_name)
        self.change_field_value("lastname", contact.last_name)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def open_contacts_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_home_page()
        self.select_first_contact()
        # submit deletion
        wd.find_element_by_css_selector("[value=Delete]").click()
        wd.switch_to_alert().accept()
        self.return_to_home_page()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    '''def modify(self):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # open contact to edit
        wd.find_element_by_css_selector('[title="Edit"]').click()
        # edit fields
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").send_keys("_edited")
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").send_keys("_edited")
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").send_keys("_edited")
        # submit edit
        wd.find_element_by_name("update").click()
        # return to home page
        self.return_to_home_page()'''

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.open_home_page()
        self.select_first_contact()
        # open modification form
        wd.find_element_by_css_selector('[title="Edit"]').click()
        # fill contact form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.return_to_home_page()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))


