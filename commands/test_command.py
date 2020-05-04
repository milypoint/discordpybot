import asyncio

from objects.command.command import Command


class TestCommand(Command):

    def action(self):
        asyncio.ensure_future(self.message.channel.send('This is `!test` command.'))

    @staticmethod
    def permissions_required():
        return ['admin']

