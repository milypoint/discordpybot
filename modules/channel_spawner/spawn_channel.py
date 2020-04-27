import tools.singleton
import client
import modules.config.pickle_handler as pickle_handler
import asyncio


@tools.singleton.singleton
class DynamicChannel(object):

    pickle_name = 'spawned_channels'

    def __init__(self):
        self.pcl = pickle_handler.PickleHandler(pickle_handler)
        self.channels = self.pcl.get()['channels'] if hasattr(self.pcl.get(), 'channels') else []
        self.spawned = self.pcl.get()['spawned'] if hasattr(self.pcl.get(), 'spawned') else []
        self.client = client.Client()
        self.guild = self.client.guilds[0]

        self.channels.append(698854759288930355)

    def on_state(self, member, before, after):
        print(before)
        print(after)
        if hasattr(after, 'channel'):
            if hasattr(before, 'channel'):
                if after.channel == before.channel:
                    return
            if after.channel.id in self.channels:
                asyncio.ensure_future(self.guild.create_voice_channel('test', category=after.channel.category))

    @staticmethod
    def create():
        pass

    @staticmethod
    def delete():
        pass