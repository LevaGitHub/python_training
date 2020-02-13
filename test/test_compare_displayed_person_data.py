import re
from random import randrange


def test_phones_on_homepage(app):
    index = randrange(len(app.person.get_person_list()))
    print("index - %s" % index)
    person_from_home_page = app.person.get_person_list()[index]
    person_from_edit_page = app.person.get_person_info_from_edit_page(index)
    assert person_from_home_page.lastname == person_from_edit_page.lastname
    assert person_from_home_page.firstname == person_from_edit_page.firstname
    assert person_from_home_page.address == person_from_edit_page.address
    person_phones_list = [person_from_edit_page.home,
                          person_from_edit_page.mobile,
                          person_from_edit_page.work,
                          person_from_edit_page.phone2]
    person_emails_list = [person_from_edit_page.email,
                          person_from_edit_page.email2,
                          person_from_edit_page.email3]
    assert person_from_home_page.all_emails_from_homepage == merge_data_on_home_page(person_emails_list)
    assert person_from_home_page.all_phones_from_homepage == merge_data_on_home_page(person_phones_list)

'''
def test_phones_on_person_view_page(app):
    index = 0
    person_from_view_page = app.person.get_person_from_view_page(index)
    person_from_edit_page = app.person.get_person_info_from_edit_page(index)
    assert person_from_view_page.home == person_from_edit_page.home
    assert person_from_view_page.mobile == person_from_edit_page.mobile
    assert person_from_view_page.work == person_from_edit_page.work
    assert person_from_view_page.phone2 == person_from_edit_page.phone2
'''


def clear(s):
    return re.sub("[() -]", "", s)


def merge_data_on_home_page(l):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, l))))
