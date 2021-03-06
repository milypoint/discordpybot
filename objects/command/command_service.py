import asyncio
import importlib
import os
import sys

import config.config as config
import objects.permission.permission_validator as permission_validator

# Importing all objects from .commands folder
for module in os.listdir(os.path.join(config.WORK_PATH, 'commands')):
    if module.endswith('.py'):
        importlib.import_module(f'commands.{module[:-3]}')


class CommandService(object):

    @staticmethod
    def command(client, message):
        """
        :param client: Client
        :param message: discord.Message
        """
        _command = message.content[1:].split()[0]

        # Getting command class object:
        for mod in [mod for mod in sys.modules if mod.startswith('commands.')]:
            if mod == f'commands.{_command}_command':
                module = importlib.import_module(mod)
                cls = getattr(module, [attr for attr in module.__dict__ if
                                       attr.startswith(_command.capitalize()) and
                                       attr.endswith('Command')
                                       ][0]
                              )
                # here we have class object in cls variable
                command_obj = cls(client, message)
                # Check if command author has permission:
                for permission in command_obj.permissions_required():
                    if not permission_validator.PermissionValidator().validate(client, message, permission):
                        asyncio.ensure_future(
                            message.channel.send(f'{message.author.mention}, you dont have `{permission}` permission')
                        )
                        return
                # Call command method after validate permission:
                command_obj.action()
                return
        # If loop out means no command handler found
        asyncio.ensure_future(
            message.channel.send(f'{message.author.mention}, command `{_command}` not found.')
        )
