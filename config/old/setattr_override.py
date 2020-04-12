from config.old.config_manager import ConfigManager


class OverrideSetAttr(object):
    """
    Class that uses for override __setattr__ module magic method

    usage:
    sys.modules[__name__] = OverrideSetAttr(globals())
    """
    def __init__(self, dic):
        vars(self).update(dic)

    def __setattr__(self, name, value):
        ConfigManager.dump(self.__name__.split('.')[-1], name, value)
        object.__setattr__(self, name, value)
