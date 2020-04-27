import logging
import os
# from modules.config.config_handler import Config
import bot_tasks.autoreboot as autoreboot
import config.config as config
import client

# Setting logger:
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename=os.path.join(os.getcwd(), config.LOG_FILE), encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
# ---


def test():
    # modules.channel_spawner.spawn_channel.DynamicChannel()
    pass



if __name__ == '__main__':
    client = client.Client()
    if config.DEBUG:
        client.loop.create_task(autoreboot.auto_reboot(client))

    # run dev test:
    test()

    # Main loop:
    client.run(config.TOKEN)
