import discord
import os
import sys

from tools import singleton
from config.config_handler import Config
from commands.command_service import CommandService


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
            CommandService().command(self, message)

    async def on_disconnect(self):
        # Restart bot.py:
        python = sys.executable
        os.execl(python, python, *sys.argv)

    async def on_voice_state_update(self, member, before, after):
        try:
            if hasattr(Config(), 'on_voice_state_update_channels') and len(Config().on_voice_state_update_channels):
                pass
        except Exception as e:
            print(e)
