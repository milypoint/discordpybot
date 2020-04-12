"""
TODO: Rewrite configuration action through class
"""

import abc


class ABCConfig(abc.ABC):

    def __init__(self):
        super().__setattr__('_attributes', dict())

    def __setattr__(self, key, value):
        self._attributes[key] = value

    def __getattr__(self, key):
        if key in self._attributes:
            return self._attributes[key]
        return None

    def __delattr__(self, key):
        if key in self._attributes:
            self._attributes.pop(key)
