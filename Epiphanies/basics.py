print(True.__class__)
print(True.__class__.__bases__)

print(bool.__mro__)

import inspect
print(inspect.getmro(type(True)))

# dir works on instances too
print(dir(5))

print(dir()) # what's in current namespace

# Imp Note:
# Simple name assignment and re-assignment are not operations on objects,
# they are namespace operations!

a = 400
b = a

assert id(a) == id(b)

del a # only removes 'a' namespace not the object it referes to

a = 1
b = 1
print(a is b) # True

a = 500
b = 500
print(a is b) # False

# it is because of CPython implementation, some ints are pre-created

# range of precreated numbers
import itertools
for i in itertools.chain(range(-7, -3), range(254, 259)):
    print(i, id(i))

i, *middle, j = 'ij' # 'i', [], 'j'

# prints the number of reference to a specific object
from sys import getrefcount as refs
print(refs(None))
