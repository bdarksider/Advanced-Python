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