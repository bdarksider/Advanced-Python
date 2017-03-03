# generator expression
g = (x for x in range(2))

print(next(g))

# generate value via generator

def prime(n):
    p = 2
    while n > 0:
        for x in range(2, p):
            if p % x == 0:
                break
        else:
            yield p
            n -= 1
        p += 1 

p = prime(3)
print(next(p))
print(next(p))
print(next(p))

# unpacking Generators

g1 = (x for x in range(3))
g2 = (x**2 for x in range(2))

print([1, *g1, 2, *g2])

# unpacking inside a set
g = (x for x in [5, 5, 6, 6])
print({*g}) # {5, 6}

# unpacking to variables
g = (x for x in range(3))
a, b, c = g 
print(a, b, c)

g = (x for x in range(6))

a, b, *c, d = g
print(a, b, d)
print(c)

a, b, * c, d = range(6)
print(a, b, d, c)

# unpacking inside a function

print(*(x for x in range(3)))

# Implement Iterable object via generator
class Count(object):
    def __init__(self, n):
        self._n = n
    def __iter__(self):
        n = self._n
        while n > 0:
            yield n
            n -= 1
    def __reversed__(self):
        n = 1
        while n <= self._n:
            yield n
            n += 1

for x in Count(5):
    print(x, end=" ")
print()

for x in reversed(Count(5)):
    print(x, end=" ")
print()

# Send message to generator
def spam():
    msg = yield
    print("Message:", msg)

try:
    g = spam()
    # start generator
    next(g)
    # send message to generator
    g.send("Hello World!")
except StopIteration:
    pass

# yield from expression 
# delegating gen do nothing(pipe)
def subgen():
    try:
        yield 2334
    except ValueError:
        print("got value error")

def delegating_gen():
    yield from subgen()

g = delegating_gen()
try:
    next(g)
    g.throw(ValueError)
except StopIteration:
    print("gen stop")

# yield from + yield from
import inspect
def subgen():
    yield from range(5)

def delegating_gen():
    yield from subgen()

g = delegating_gen()
print(inspect.getgeneratorstate(g)) # 'GEN_CREATED'
print(next(g))
print(next(g))

print(inspect.getgeneratorstate(g))
g.close()
print(inspect.getgeneratorstate(g))

# yield (from) EXPR return RES
def average():
    total = 0
    count = 0
    avg = None
    while True:
        val = yield
        if not val:
            break
        total += val
        count += 1
        avg = total / count
    return avg

g = average()
next(g) # start gen

g.send(3)
g.send(5)

try:
    g.send(None)
except StopIteration as e:
    ret = e.value

print(ret)

# yield from EXP return RES
def subgen():
    yield 9523

def delegating_gen():
    yield from subgen()
    return 3344

try:
    g = delegating_gen()
    next(g)
    next(g)
except StopIteration as _e:
    print(_e.value)

# Generate sequences
# get a list via generator
def chain():
    for x in 'ab':
        yield x
    for x in range(3):
        yield x

a = list(chain())
print(a)

# equivalent to 
def chain():
    yield from 'ab'
    yield from range(3)

a = list(chain())
print(a)

# RES = yield from EXP explaination
def subgen():
    for x in range(3):
        yield x

EXP = subgen()
def delegating_gen():
    _i = iter(EXP)
    try:
        _y = next(_i)
        print("line 1", _y)
    except StopIteration as _e:
        RES = _e.value
    else:
        while True:
            _s = yield _y
            try:
                _y = _i.send(_s)
            except StopIteration as _e:
                RES = _e.value
                break

g = delegating_gen()
print(next(g))
print(next(g))
print(next(g))

