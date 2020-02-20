import fixture.general as general
import os.path
import json
from model.group import Group
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


test_data = [
    Group(name=general.generate_sequence(20, general.test_seq, prefix='name'),
          header=general.generate_sequence(20, general.test_seq, prefix='header'),
          footer=general.generate_sequence(20, general.test_seq, prefix='footer'))
    for _ in range(n)
]

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file_path, "w") as out:
    out.write(json.dumps(test_data, default=lambda x: x.__dict__, indent=2))
