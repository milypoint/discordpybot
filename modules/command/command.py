import abc


class Command(abc.ABC):
    """
    Note:
    For call a coroutine function use asyncio.ensure_future(coro())
    """

    @abc.abstractmethod
    def action(self):
        pass

    def __init__(self, client, message):
        super().__setattr__('_attributes', dict())
        self.client = client
        self.message = message

    def __setattr__(self, key, value):
        super().__getattribute__('_attributes')[key] = value

    def __getattr__(self, key):
        return super().__getattribute__('_attributes')[key]

    @staticmethod
    def permissions_required():
        return []
