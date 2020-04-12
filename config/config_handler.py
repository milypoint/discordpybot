import sys
import os
import pickle
import asyncio

from config import config
from tools.singleton import singleton


@singleton
class Config(object):

    def __init__(self):
        super().__setattr__('_config', dict())
        for k, v in config.config.items():
            self.__setattr__(k, v)

    def __setattr__(self, key, value):
        super().__getattribute__('_config')[key] = value

    def __getattr__(self, key):
        return super().__getattribute__('_config')[key]

    @staticmethod
    def __load_pickle(file):
        _dict = {}
        if os.path.getsize(file) > 0:
            with open(file, 'rb') as f:
                _dict = pickle.load(f)
        return _dict

    def __update_config_channel(self):
        asyncio.ensure_future(self.client.wait_until_ready())

