import os.path
import jsonpickle
from model.person import Person
import getopt
import sys
import string
import fixture.general as general

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["count of persons", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 3
f = "data/persons.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


test_data = [
    Person(firstname=general.generate_sequence(20, general.test_seq, prefix='firstname'),
           middlename=general.generate_sequence(20, general.test_seq, prefix='middlename'),
           lastname=general.generate_sequence(20, general.test_seq, prefix='lastname'),
           nickname=general.generate_sequence(20, general.test_seq),
           title=general.generate_sequence(20, general.test_seq),
           company=general.generate_sequence(20, general.test_seq),
           address=general.generate_sequence(20, general.test_seq),
           home=general.generate_sequence(2, string.digits),
           mobile=general.generate_sequence(11, string.digits),
           work=general.generate_sequence(20, general.test_seq),
           fax=general.generate_sequence(11, string.digits),
           email=general.generate_sequence(20, general.test_seq),
           email2=general.generate_sequence(20, general.test_seq),
           email3=general.generate_sequence(20, general.test_seq),
           homepage=general.generate_sequence(20, general.test_seq),
           bday=general.choice(general.days),
           bmonth=general.choice(general.months),
           byear=general.choice(general.years),
           aday=general.choice(general.days),
           amonth=general.choice(general.months),
           ayear=general.choice(general.years),
           address2=general.generate_sequence(20, general.test_seq),
           phone2=general.generate_sequence(11, string.digits),
           notes=general.generate_sequence(50, general.test_seq))
    for _ in range(n)
]

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file_path, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(test_data))