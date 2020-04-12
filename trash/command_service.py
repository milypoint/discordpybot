import os
import sys
import importlib
import asyncio
import re

from config import config
from permissions.permission_validator import PermissionValidator

# Importing all modules from .commands folder
for module in os.listdir(os.path.join(config.WORK_PATH, 'commands')):
    if module.endswith('.py'):
        importlib.import_module(f'commands.{module[:-3]}')


class CommandService(object):

    # Regex realization. Probably works slower. Did just for fun.
    @staticmethod
    def command(client, message):
        # Match command pattern "!<command> <context>"
        m = re.match(r"!(?P<command>[a-zA-Z0-9_]+)( +(?P<context>.*))?", message.content)
        if m is not None:
            _command = m.group('command')
            _context = m.group('context')

            # Getting command class object:
            _module = [mod for mod in sys.modules if re.match(rf"(commands)(\.)({_command})(_command)", mod)]
            if not len(_module):
                asyncio.ensure_future(
                    message.channel.send(f'{message.author.mention}, command `{_command}` not found.')
                )
                return
            module = importlib.import_module(_module[0])
            try:
                cls = getattr(module,
                              [attr for attr in module.__dict__ if
                               re.match(rf"{_command.capitalize()}(Command)", attr)][0]
                              )
            except IndexError as error:
                print(f'Exception catch: {error}')
                return
            command_obj = cls(client, message)
            for permission in command_obj.permissions_required():
                if not PermissionValidator().validate(client, message, permission):
                    asyncio.ensure_future(
                        message.channel.send(f'{message.author.mention}, you dont have `{permission}` permission')
                    )
                    return
            # Call command method after validate permissions:
            command_obj.action()






