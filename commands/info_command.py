import asyncio

from .command import Command


class InfoCommand(Command):

    def action(self):
        content = self.message.content[len('!info_'):]
        if not len(content):
            channels = [self.message.channel]
        else:
            channels = [channel for channel in self.message.guild.channels if channel.name == content]
        if not len(channels):
            asyncio.ensure_future(
                self.message.channel.send(
                    f'{self.message.author.mention}, Channel with name `{content}` not found.'
                )
            )
            return

        response = f'{self.message.author.mention},'
        for channel in channels:
            response += ('\n' +
                         f'__**name**__:  `{channel.name}`' + '\n' +
                         f'id:  `{channel.id}`' + '\n' +
                         f'type:  `{channel.type}`' + '\n' +
                         f'category:  `{channel.category}`')
        asyncio.ensure_future(self.message.channel.send(response))

    @staticmethod
    def permissions_required():
        return ['admin']

