class Example(object):
    def __init__(self):
        self.name = "ex"
    def printex(self):
        print("This is an example")

ex = Example()

print(hasattr(ex, "name"))  # True
print(hasattr(ex, "printex")) # True
print(hasattr(ex, "print")) # False

print(getattr(ex, 'name')) # 'ex'

setattr(ex, 'name', 'example')

print(ex.name) # 'example'

class Cat(Example):
    pass

tess = Cat()

print(issubclass(Cat, Example)) # True

print(globals())

class ExampleClass():
    pass 

def example_function():
    pass 

ex = ExampleClass()

print(ex.__class__.__name__) # ExampleClass

# __new__ & __init__
# need to further research on this code
class ClassA(object):
    def __new__(cls, arg):
        print('__new__ ' + arg)
        return object.__new__(cls)
    def __init__(self, arg):
        print('__init__ ' + arg)

o = ClassA("Hello")

# init won't be invoked 
class ClassB(object):
    def __new__(cls, arg):
        print('__new__' + arg)
        return object 
    def __init__(self, arg):
        print("__init__", arg)

o = ClassB("Hello")

# The diamond problem

def foo_a(self):
    print("This is ClsA")
def foo_b(self):
    print("This is ClsB")
def foo_c(self):
    print("This is ClsC")

class Type(type):
    def __repr__(cls):
        return cls.__name__

ClsA = Type("ClsA", (object,), {'foo': foo_a})
ClsB = Type("ClsB", (ClsA,), {'foo': foo_b})
ClsC = Type("ClsC", (ClsA,), {'foo': foo_c})
ClsD = Type("ClsD", (ClsB, ClsC), {})

print(ClsD.mro())

print(ClsD().foo())

s = "This is a very very very very long python string"

print(s)

s = "This is a very very very " \
    "long python string"

print(s)

s = ("this is a very very" +  
    "very long python string")

print(s)

# using slice object
s = slice(0, -1, 2)

a = list(range(10))

print(a[s])

# filter
l = ['1', '2', 3, 'Hello', 4]
predicate = lambda x: isinstance(x, int)

print(list(filter(predicate, l)))

a = {"1": 1, "2": 2, "3": 3}
b = {"2": 2, "3": "amaze", "4": 4}

c = set(a).intersection(set(b))
print(c)

a.update(b)

print(a) # {'3': 'amaze', '1': 1, '2': 2, '4': 4} 
# if key matches value is replaced by second dict

# dict comprehension

a = {'{0}'.format(x): x for x in range(3)}

print(a)

a = {x: x for x in range(3)}

print(a)

# using map
fn = lambda x: x**2
print(list(map(fn, range(5))))

# namedtuple
from collections import namedtuple
Example = namedtuple("Example", 'a b c')

e = Example(1,2,3)

print(e.a, e[1], e[1] + e.b)

print(type(e)) # class without methods

# __iter__
class Example(object):
    def __init__(self, list_):
        self._list = list_
    def __iter__(self):
        return iter(self._list)

ex = Example(list(range(5)))

for i in ex:
    print(i, end=" ")
print()

# generator as Iterator

a = (_ for _ in range(10))
for _ in a: print(_, end=" ")
print()

# equivalent to
def generator():
    for _ in range(10):
        yield _

for _ in generator(): print(_, end=" ")
print()

# Emulating a list
class EmuList(object):
    def __init__(self, list_):
        self._list = list_
    def __repr__(self):
        return "EmuList: " + repr(self._list)
    def append(self, item):
        self._list.append(item)
    def remove(self, item):
        self._list.remove(item)
    def __len__(self):
        return len(self._list)
    def __getitem__(self, sliced):
        print(sliced) # slice() object
        return self._list[sliced]
    def __setitem__(self, sliced, val):
        self._list[sliced] = val 
    def __delitem__(self, sliced):
        del self._list[sliced]
    def __contains__(self, item):
        return item in self._list
    def __iter__(self):
        return iter(self._list)

emul = EmuList(list(range(5)))
print(emul)

# __getitem__
print(emul[1:3])

# __len__
print(len(emul))

emul.append(5)
print(emul)

# Emulating a dictionary 
class EmuDict(object):
    def __init__(self, dict_):
        self._dict = dict_
    def __repr__(self):
        return "EmuDict: " + repr(self._dict)
    def __getitem__(self, key):
        return self._dict[key]
    def __setitem__(self, key, val):
        self._dict[key] = val
    def __delitem__(self, key, val):
        del self._dict[key]
    def __contains__(self, key):
        return key in self._dict
    def __iter__(self):
        return iter(self._dict.keys())

_ = {"1": 1, "2": 2, "3": 3}
emud = EmuDict(_)

print(emud) # __repr__

# Emulating matrix multiplication
# > Python3.5

class Arr:
    def __init__(self, *arg):
        self._arr = arg 
    def __matmul__(self, other):
        if not isinstance(other, Arr):
            raise TypeError
        if len(self) != len(other):
            raise ValueError
        return sum([x*y for x, y in zip(self._arr, other._arr)])
    def __imatmul__(self, other):
        if not isinstance(other, Arr):
            raise TypeError
        if len(self) != len(other):
            raise ValueError
        res = sum([x*y for x, y in zip(self._arr, other_arr)])
        self._arr = [res]
        return self 
    def __len__(self):
        return len(self._arr)
    def __str__(self):
        return self.__repr__()
    def __repr__(self):
        return "Arr({})".format(repr(self._arr))

a = Arr(9, 5, 2, 7)
b = Arr(5, 5, 6, 6)

print(a @ b) # __matmul__

# decorator
from functools import wraps
def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Before calling {}.".format(func.__name__))
        ret = func(*args, **kwargs)
        print("After calling {}.".format(func.__name__))
        return ret
    return wrapper

@decorator
def example():
    print("Inside example function")

example()

# decorator with arguments
from functools import wraps
def decorator_with_argument(val):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("Val is {0}".format(val))
            return func(*args, **kwargs)
        return wrapper
    return decorator

@decorator_with_argument(10)
def example():
    print("This is example function")

example()

print((lambda x: x**2)(3))

# Option arguments
def example(a, b=None, *args, **kwargs):
    print(a, b)
    print(args)
    print(kwargs)

a_tuple = (1,2,3,4,5)
a_dict = {"1": 1, "2": 2, "3": 3}

example(1, "var", *a_tuple, **a_dict)

# type() declare (create) a class
# the practical use of this style is questionable
def fib(self, n):
    if n <= 2:
        return 1
    return fib(self, n-1) + fib(self, n-2)

Fib = type('Fib', (object,), {'val': 10, 'fib': fib})

f = Fib()

print(f.val) # 10

print(f.fib(f.val))

# Callable object 
class CallableObject(object):
    def example(self, *args, **kwargs):
        print("I am callable!")
    def __call__(self, *args, **kwargs):
        self.example(*args, **kwargs)

ex = CallableObject()
ex()

# using @contextmanager
from contextlib import contextmanager

@contextmanager
def opening(filename, mode='r'):
    f = open(filename, mode)
    try:
        yield f
    finally:
        f.close()

with opening('text.txt') as fd:
    fd.read()

with open("text.txt") as fd:
    fd.read()