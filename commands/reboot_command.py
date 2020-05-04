import asyncio

from objects.command.command import Command


class RebootCommand(Command):

    def action(self):
        asyncio.ensure_future(self.client.logout())

    @staticmethod
    def permissions_required():
        return ['admin']