import re


def test_phones_on_homepage(app, db):
    person_from_home_page = app.person.get_all_person_list_from_homepage()
    for each in person_from_home_page:
        try:
            print(each)
            person_from_db = db.get_person(each.person_id)
            assert each.lastname == person_from_db.lastname
            assert each.firstname == person_from_db.firstname
            assert each.address == person_from_db.address
            person_phones_list = [person_from_db.home,
                                  person_from_db.mobile,
                                  person_from_db.work,
                                  person_from_db.phone2]
            person_emails_list = [person_from_db.email,
                                  person_from_db.email2,
                                  person_from_db.email3]
            assert each.all_emails_from_homepage == merge_data_on_home_page(person_emails_list)
            assert each.all_phones_from_homepage == merge_data_on_home_page(person_phones_list)
        except AssertionError as err:
            print("AssertionError - {}".format(err))


def clear(s):
    return re.sub("[() -]", "", s)


def merge_data_on_home_page(l):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, l))))
