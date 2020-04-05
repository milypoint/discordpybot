import discord
import logging
import os
import sys


from config import config
from commands.command_service import CommandService
if config.DEBUG:
    from bot_tasks import autoreboot

# Setting logger:
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename=os.path.join(os.getcwd(), config.LOG_FILE), encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
# ---

client = discord.Client(status="online")


@client.event
async def on_ready():
    print('Logged in as', client.user.name, "(id " + str(client.user.id) + ")", end='\n\n')


@client.event
async def on_message(message):
    await client.wait_until_ready()
    if message.author.id != client.user.id:
        print('call on_message event:')
        print(f'message.content "{message.content}" message.author.id "{message.author.id}"')

    if message.content.strip().startswith('!'):
        CommandService().command(client, message)


@client.event
async def on_disconnect():
    # Restart bot.py:
    python = sys.executable
    os.execl(python, python, *sys.argv)


if __name__ == '__main__':
    if config.DEBUG:
        client.loop.create_task(autoreboot.auto_reboot(client))

    # Main loop:
    client.run(config.token)
