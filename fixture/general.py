from random import choice
import string

days = [i for i in range(1, 32)]
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
          "December"]
years = [i for i in range(1970, 2000)]


test_seq = string.ascii_letters + string.digits + " " * 10


def generate_sequence(size, seq, prefix=''):
    return prefix + ''.join(choice(seq) for _ in range(size))
