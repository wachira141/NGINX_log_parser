#!/usr/bin/env python3
import time
import random
import sys
import string

def gen_inserter():
    '''
    generate insertion values
    '''
    for i in range(30, 100):
        name = ''.join(random.choice(string.ascii_letters) for x in range(15))
        f_name = name[:5]
        l_name = name[6:]
        id_num = i
        time.sleep(1)
        sys.stdout.write("INSERT INTO users VALUES({}, '{} {}', {}, '{}-{}-{}', '{}@email.com');\n".format( i, f_name, l_name, random.randint(1, 80), random.randint(1900, 2023), random.randint(1, 12), random.randint(1, 31), f_name))
        sys.stdout.flush

if __name__ == '__main__':
    gen_inserter()
