

class PermissionValidator(object):

    @staticmethod
    def validate(client, message, permission):
        if hasattr(message, 'guild'):
            guild_roles = [role.name for role in message.guild.roles]
        else:
            guild_roles = [role.name for role in client.guilds[0].roles]

        # Check if permission exists:
        if permission not in guild_roles:
            print(f'Unknown permission: {permission}')
            return False

        # Check if author has required permissions
        if permission not in [role.name for role in message.author.roles]:
            print(f'User {message.author} dont have required permission: {permission}')
            return False

        return True
