class Vector:

    def __init__(self, **coords):
        # prefix with _ for making attributes private
        private_coords = {'_' + k: v for k, v in coords.items()}
        self.__dict__.update(private_coords)

    def __getattr__(self, name):
        private_name = '_' + name
        # EAFP style programming
        try:
            return self.__dict__[private_name]
        except KeyError:
            if private_name not in self.__dict__:
                raise AttributeError('{!r} object has not attributes {!r}'.format(
                        self.__class__, name))

    def __setattr__(self, name, value):
        raise AttributeError("Can't set attribute {!r}".format(name))

    def __delattr__(self, name):
        raise AttributeError("Can't delete attribute {!r}".format(name))

    def __repr__(self):
        # slice string for removing _ while printing
        return "{}({})".format(
            self.__class__.__name__,
            ', '.join("{k}={v}".format(
                k=k[1:],
                v=self.__dict__[k])
                for k in sorted(self.__dict__.keys())))
