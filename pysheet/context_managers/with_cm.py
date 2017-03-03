from threading import Lock
lock = Lock()

def do_something_dangerous():
    with lock:
        raise Exception('oops I forgot this code coudl raise exception')

try:
    do_something_dangerous()
except:
    print('Got an exception')

lock.acquire()

print('Got here')

# exploring contextlib

''' decorate a generator function that calls yield exactly once. 
Everything before the call to yield is considered the code 
for __enter__(). Everything after is the code for __exit__()'''

from contextlib import contextmanager

@contextmanager
def open_file(path, mode):
    the_file = open(path, mode)
    yield the_file
    the_file.close()

files = []

for x in range(10000):
    with open_file('text.txt', 'w') as infile:
        files.append(infile)

for f in files:
    if not f.closed:
        print('not closed')

# offical python docs example
@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("<%s>" % name)

with tag("h1"):
    print("foo")

''' lets you define a context manager using the class-based approach, 
but inheriting from contextlib.ContextDecorator. By doing so, you 
can use your context manager with the with statement as normal 
or as a function decorator '''

from contextlib import ContextDecorator

class makeparagraph(ContextDecorator):
    def __enter__(self):
        print('<p>')
        return self

    def __exit__(self, *exc):
        print('</p>')
        return False

@makeparagraph()
def emit_html():
    print('Here is some non-HTML')

emit_html()