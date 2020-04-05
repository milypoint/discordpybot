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
        self.client = client
        self.message = message

    @staticmethod
    def permissions_required():
        return []
