# class Example(object):
#     def __init__(self, value):
#         self._val = value
#     @property
#     def val(self):
#         return self._val
#     @val.setter
#     def val(self, value):
#         if not isinstance(value, int):
#             raise TypeError("Expected int")
#         self._val = value
#     @val.deleter
#     def val(self):
#         print("found me")
#         del self._val

# ex = Example(123)
# del ex.val
# next line throws error if 
# ex.val = "str"

# equivalent to 
class Example(object):
    def __init__(self, value):
        self._val = value

    def _val_getter(self):
        return self._val

    def _val_setter(self, value):
        if not isinstance(value, int):
            raise TypeError("Expected int")
        self._val = value

    def _val_deleter(self):
        del self.val

    val = property(fget=_val_getter, fset=_val_setter, 
                   fdel=_val_deleter, doc=None)

# have to add example to show how to set value
