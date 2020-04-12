import asyncio

from .command import Command
from config import config


class ConfigCommand(Command):

    def action(self):
        content = self.message.content.split()[1:]

        # if len(content) == 0:
        #     # TODO: return all config data
        #     pass

        if len(content) == 1:
            asyncio.ensure_future(self.message.channel.send(
                f'{self.message.author.mention}, {content[0]}: {str(getattr(config, content[0]))}'
            ))
        # if len(content) == 2:
        #     setattr(config, content[0], content[1])
        #     asyncio.ensure_future(self.message.channel.send(f'{self.message.author.mention}, success!'))
        # return

    @staticmethod
    def permissions_required():
        return ['admin']

