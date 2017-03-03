# amazing pattern
class Integer(object):
    def __init__(self, name):
        self._name = name
    def __get__(self, inst, cls):
        print(inst)
        if inst is None:
            return self
        else:
            return inst.__dict__[self._name]
    def __set__(self, inst, value):
        if not isinstance(value, int):
            raise TypeError("Expected int")
        inst.__dict__[self._name] = value
    def __delete__(self, inst):
        del inst.__dict__[self._name]

class Example(object):
    x = Integer('x')

    def __init__(self, val):
        self.x = val

ex1 = Example(1)
print(ex1.x) # 1

# next line throws error
# ex2 = Example("str")

ex3 = Example(3)
print(hasattr(ex3, 'x'))
del ex3.x
# doesn't work in python3 -- have to check
print(hasattr(ex3, 'x'))
