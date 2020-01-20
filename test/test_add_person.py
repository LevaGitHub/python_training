# -*- coding: utf-8 -*-

import random
import string
from model.person import Person

days = [i for i in range(1, 32)]
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
          "December"]
years = [i for i in range(1970, 2000)]


def generate_chars_sequence(size, seq):
    return ''.join(random.choice(seq) for _ in range(size))


def test_add_person(app):
    app.session.login(username="admin", password="secret")
    app.person.open_person_page()
    pers = Person(firstname=generate_chars_sequence(20, string.ascii_letters),
                  middlename=generate_chars_sequence(20, string.ascii_letters),
                  lastname=generate_chars_sequence(20, string.ascii_letters),
                  nickname=generate_chars_sequence(20, string.ascii_letters),
                  title=generate_chars_sequence(20, string.ascii_letters),
                  company=generate_chars_sequence(20, string.ascii_letters),
                  address=generate_chars_sequence(20, string.ascii_letters),
                  home=generate_chars_sequence(2, string.digits),
                  mobile=generate_chars_sequence(11, string.digits),
                  work=generate_chars_sequence(20, string.ascii_letters),
                  fax=generate_chars_sequence(11, string.digits),
                  email=generate_chars_sequence(20, string.ascii_letters),
                  email2=generate_chars_sequence(20, string.ascii_letters),
                  email3=generate_chars_sequence(20, string.ascii_letters),
                  homepage=generate_chars_sequence(20, string.ascii_letters),
                  bday=random.choice(days),
                  bmonth=random.choice(months),
                  byear=random.choice(years),
                  aday=random.choice(days),
                  amonth=random.choice(months),
                  ayear=random.choice(years),
                  address2=generate_chars_sequence(20, string.ascii_letters),
                  phone2=generate_chars_sequence(11, string.digits),
                  notes=generate_chars_sequence(50, string.ascii_letters))
    app.person.input_person_data(pers)
    app.person.return_to_home_page()
    app.session.logout()
