import os
import pickle


class ConfigManager(object):
    """
    Class that uses pickle module for store data objects in files
    """

    @classmethod
    def dump(cls, config_name, key, value):
        file = cls.file_name(config_name)
        _dict = cls.load(config_name)
        _dict[key] = value
        with open(file, 'wb') as f:
            pickle.dump(_dict, f, pickle.HIGHEST_PROTOCOL)

    @classmethod
    def wipe(cls, config_name):
        file = cls.file_name(config_name)
        with open(file, 'wb') as f:
            pickle.dump(dict(), f, pickle.HIGHEST_PROTOCOL)

    @classmethod
    def load(cls, config_name):
        file = cls.file_name(config_name)
        _dict = {}
        if os.path.getsize(file) > 0:
            with open(file, 'rb') as f:
                _dict = pickle.load(f)
        return _dict

    @staticmethod
    def file_name(config_name):
        return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pickle', f'{config_name}.pcl')
