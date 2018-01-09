class Vector:

    def __init__(self, **coords):
        # prefix with _ for making attributes private
        private_coords = {'_' + k: v for k, v in coords.items()}
        self.__dict__.update(private_coords)

    def __repr__(self):
        # slice string for removing _ while printing
        return "{}({})".format(
            self.__class__.__name__,
            ', '.join("{k}={v}".format(
                k=k[1:],
                v=self.__dict__[k])
                for k in sorted(self.__dict__.keys())))