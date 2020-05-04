import os
import pickle


class PickleHandler(object):
    """
    Simple handler to use Pickle module.

    __init__ does load data from pcl file.
    Whenever adds new attribute calls dump method.
    """

    _properties = ['file']

    def __init__(self, file):
        super().__setattr__('_attributes', dict())
        self.file = file
        for key, value in self.__load().items():
            self.__setattr__(key, value)

    def __setattr__(self, key, value):
        if key in self.__class__._properties:
            super().__setattr__(key, value)
        else:
            super().__getattribute__('_attributes')[key] = value
            self.__dump()

    def __getattr__(self, key):
        if key in self.__class__._properties:
            return super().__getattribute__(key)
        return super().__getattribute__('_attributes')[key]

    def __load(self):
        _dict = {}
        if os.path.isfile(self.file):
            if os.path.getsize(self.file) > 0:
                with open(self.file, 'rb') as f:
                    _dict = pickle.load(f)
        return _dict

    def __dump(self):
        with open(self.file, 'wb') as f:
            pickle.dump(super().__getattribute__('_attributes'), f, pickle.HIGHEST_PROTOCOL)

    def get(self):
        return super().__getattribute__('_attributes')
