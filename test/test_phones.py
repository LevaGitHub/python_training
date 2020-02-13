import re


def test_phones_on_homepage(app):
    index = 0
    person_from_home_page = app.person.get_person_list()[index]
    person_from_edit_page = app.person.get_person_info_from_edit_page(index)
    assert person_from_home_page.all_phones_from_homepage == merge_phones_like_on_home_page(person_from_edit_page)

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


def merge_phones_like_on_home_page(person):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [person.home, person.mobile, person.work, person.phone2]))))
