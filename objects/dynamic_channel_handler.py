import discord

import helpers.discord_objects as do
import helpers.singleton as singleton


@singleton.singleton
class DynamicChannelHandler(object):
    """
    Class that handle creation temporary voice channels.
    """

    main_dynamic_channels = [
        706656862610653219
    ]

    async def action(self,
                     member: discord.Member,
                     before: discord.VoiceState,
                     after: discord.VoiceState
                     ):

        # Check if channel does`t changed
        try:
            if after.channel.id == before.channel.id:  # same channel
                return
        except AttributeError as e:
            pass

        # Check if connected to main channel
        if hasattr(after, 'channel') and after.channel is not None:
            if after.channel.id in self.main_dynamic_channels:
                new_channel = await self.create('test', after.channel.category)
                if new_channel is not None:
                    await member.move_to(new_channel)

        # Check if disconnected from temporary channel
        if hasattr(before, 'channel') and before.channel is not None:
            if (before.channel.category.name == 'dynamic' and
                    before.channel.id not in self.main_dynamic_channels and
                    len(before.channel.members) == 0):
                await self.delete(before.channel)

    @staticmethod
    async def create(name: str, category: discord.CategoryChannel):
        try:
            guild = do.guild()
            return await guild.create_voice_channel(name, category=category)
        except Exception as e:
            print(e)
            return

    @staticmethod
    async def delete(channel: discord.VoiceChannel):
        await channel.delete()
