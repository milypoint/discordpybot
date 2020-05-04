import sys

import discord

import config.config as config
import helpers.singleton as singleton
import objects.command.command_service
import objects.dynamic_channel_handler


@singleton.singleton
class Client(discord.Client):

    async def on_ready(self):
        print('Logged in as', self.user.name, "(id " + str(self.user.id) + ")", end='\n\n')

    async def on_message(self, message):
        """
        :param message: discord.Message
        """
        await self.wait_until_ready()

        if message.author.id != self.user.id:
            print('call on_message event:')
            print(f'message.content "{message.content}" message.author.id "{message.author.id}"')

        if message.content.strip().startswith('!'):
            objects.command.command_service.CommandService().command(self, message)

    @staticmethod
    async def on_disconnect():
        print('Disconnected.')

    async def on_voice_state_update(self, member, before, after):
        """
        :param member: discord.Member
        :param before: discord.VoiceState
        :param after: discord.VoiceState
        """
        await self.wait_until_ready()
        await objects.dynamic_channel_handler.DynamicChannelHandler().action(member, before, after)
