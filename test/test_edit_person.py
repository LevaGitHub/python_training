import string
import fixture.general as general
from model.person import Person


def test_edit_person(app):
    pers = Person(firstname=general.generate_chars_sequence(20, string.ascii_letters),
                  middlename=general.generate_chars_sequence(20, string.ascii_letters),
                  lastname=general.generate_chars_sequence(20, string.ascii_letters),
                  nickname=general.generate_chars_sequence(20, string.ascii_letters),
                  title=general.generate_chars_sequence(20, string.ascii_letters),
                  company=general.generate_chars_sequence(20, string.ascii_letters),
                  address=general.generate_chars_sequence(20, string.ascii_letters),
                  home=general.generate_chars_sequence(2, string.digits),
                  mobile=general.generate_chars_sequence(11, string.digits),
                  work=general.generate_chars_sequence(20, string.ascii_letters),
                  fax=general.generate_chars_sequence(11, string.digits),
                  email=general.generate_chars_sequence(20, string.ascii_letters),
                  email2=general.generate_chars_sequence(20, string.ascii_letters),
                  email3=general.generate_chars_sequence(20, string.ascii_letters),
                  homepage=general.generate_chars_sequence(20, string.ascii_letters),
                  bday=general.choice(general.days),
                  bmonth=general.choice(general.months),
                  byear=general.choice(general.years),
                  aday=general.choice(general.days),
                  amonth=general.choice(general.months),
                  ayear=general.choice(general.years),
                  address2=general.generate_chars_sequence(20, string.ascii_letters),
                  phone2=general.generate_chars_sequence(11, string.digits),
                  notes=general.generate_chars_sequence(50, string.ascii_letters))
    app.person.edit_first_person(pers)
