import discord
import os
import sys

import tools.singleton as singleton
import config.config as config
import modules.command.command_service
import modules.channel_spawner.spawn_channel



@singleton.singleton
class Client(discord.Client):
    async def on_ready(self):
        print('Logged in as', self.user.name, "(id " + str(self.user.id) + ")", end='\n\n')

    async def on_message(self, message):
        await self.wait_until_ready()
        if message.author.id != self.user.id:
            print('call on_message event:')
            print(f'message.content "{message.content}" message.author.id "{message.author.id}"')

        if message.content.strip().startswith('!'):
            modules.command.command_service.CommandService().command(self, message)

    async def on_disconnect(self):
        # Restart bot.py:
        python = sys.executable
        os.execl(python, python, *sys.argv)

    async def on_voice_state_update(self, member, before, after):
        modules.channel_spawner.spawn_channel.DynamicChannel().on_state(member, before, after)
        # print(after)
