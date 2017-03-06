import time
from contextlib import contextmanager

@contextmanager
def profile(msg):
    try:
        s = time.time()
        yield
    finally:
        e = time.time()
        print('{} cost time: {}'.format(msg, e - s))

with profile('block1'):
    time.sleep(1)

with profile('block2'):
    time.sleep(3)
