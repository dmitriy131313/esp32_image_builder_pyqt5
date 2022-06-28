import re

class Integer:
    def __set_name__(self, owner, name):
        self.name = "__" + name

    def __get__(self, instance, owner):
        if instance.__dict__[self.name] == None:
            raise ValueError('offset or size is not set')
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value != None:
            raw_hex = re.sub(r'^0[xX]', "", str(value))
            val = re.search(r'[^0-9a-fA-F]', raw_hex)
            if val != None:
                raise ValueError('offset or size should be in hexadecimal')

        instance.__dict__[self.name] = value

class Partition:
    offset = Integer()
    len    = Integer()

    def __init__(self) -> None:
        self.__f_name   = None
        self.__f_path   = None
        self.offset   = None
        self.len      = None

    @property
    def name(self):
        return self.__f_name

    @name.setter
    def name(self, name):
        self.__f_name = name

    @property
    def path(self):
        return self.__f_path

    @path.setter
    def path(self, path):
        self.__f_path = path