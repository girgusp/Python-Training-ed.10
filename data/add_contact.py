from model.contact import Contact
import random
import string


constant = [
    Contact(first_name="first_name1", last_name="last_name1"),
    Contact(first_name="first_name2", last_name="last_name2")
]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    Contact(first_name=random_string("first_name", 10))
    for first_name in ["", random_string("name", 10)]
]