import os
import asyncio

import objects.config.pickle_handler as ph


class Config(object):
    """
    Class that override behavior of config module.

    Add "sys.modules[__name__] = ch.Config(globals())" at the end of config file.

    After that config module able to store new attributes in pickle files. For example: module config/config.py has
    code:

    SOF
    attr_1 = "val_1"
    attr_2 = "val_2"
    EOF

    If add new attribute config.attr_3 = "val_3" than this item handles by pickle module and saves by in
    config/config.pcl
    """

    def __init__(self, dic):
        vars(self).update(dic)  # save external attributes
        super().__setattr__('_config', dict())
        pcl = self.get_pcl()
        for k, v in pcl.get().items():
            setattr(self, k, v)

    def __setattr__(self, key, value):
        super().__getattribute__('_config')[key] = value
        setattr(self.get_pcl(), key, value)

    def __getattr__(self, key):
        return super().__getattribute__('_config')[key]

    def get_config(self):
        """
        Returns whole config data
        :return: []
        """
        return super().__getattribute__('_config')

    def get_name(self):
        """
        Returns the name based on the name of the file that was overridden by this class.
        :return: str
        """
        return str(self.__file__).split('/')[-1].split('.')[0]

    def get_pcl(self):
        if not hasattr(super(), 'pcl'):
            super().__setattr__('pcl',
                                ph.PickleHandler(
                                    os.path.join(os.path.dirname(os.path.abspath(__file__)), f'{self.get_name()}.pcl')
                                    ))
        return super().__getattribute__('pcl')

    def __update_config_channel(self, client):
        asyncio.ensure_future(client.wait_until_ready())
