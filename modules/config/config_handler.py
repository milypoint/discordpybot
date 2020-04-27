import sys
import os
import pickle
import asyncio

import config.config
import tools.singleton


@tools.singleton.singleton
class Config(object):

    def __init__(self):
        super().__setattr__('_config', dict())
        for item in dir(config.config):
            if item.isupper():
                self.__setattr__(item, object.__getattribute__(config.config, item))

    def __setattr__(self, key, value):
        super().__getattribute__('_config')[key] = value

    def __getattr__(self, key):
        return super().__getattribute__('_config')[key]

    def get_config(self):
        return super().__getattribute__('_config')

    @staticmethod
    def __load_pickle(file):
        _dict = {}
        if os.path.getsize(file) > 0:
            with open(file, 'rb') as f:
                _dict = pickle.load(f)
        return _dict

    def __update_config_channel(self, client):
        asyncio.ensure_future(client.wait_until_ready())
