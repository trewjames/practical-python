# typedproperty.py

def string(name):
    return typedproperty(name, str)


def integer(name):
    return typedproperty(name, int)


def float(name):
    return typedproperty(name, (int, float))


def typedproperty(name, expected_type):
    private_name = '_' + name

    @property
    def prop(self):
        return getattr(self, private_name)

    @prop.setter
    def prop(self, value):
        if not isinstance(value, expected_type):
            raise TypeError(f"Expected {expected_type}")
        if isinstance(expected_type, tuple):
            setattr(self, private_name, float(value))
        else:
            setattr(self, private_name, value)

    return prop
