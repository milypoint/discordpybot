import asyncio

from .command import Command


class RebootCommand(Command):

    def action(self):
        asyncio.ensure_future(self.client.logout())
