#!/usr/bin/env python3
import random
from datetime import datetime
import time
import sys

def run():
    '''function to create a faker logger files
    '''
    for i in range(10000000):
        time.sleep(2)
        log = '{:d}.{:d}.{:d}.{:d} -- [{}] "GET /{}/{} HTTP/1.1" {} {}\n'\
            .format(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255), random.randint(1, 255),  datetime.now(),random.choice(['status', 'home', 'profile']), random.randint(20, 77),random.choice([200, 201, 300, 301, 400, 404, 500]),random.randint(1, 1024))
        sys.stdout.write(log)
        sys.stdout.flush()


if __name__ == "__main__":
    run()
