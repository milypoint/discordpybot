import logging
import os
import sys
import asyncio

import bot_tasks.autoreboot as autoreboot
import config.config as config
from objects import client

# Setting logger:
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename=os.path.join(os.getcwd(), config.LOG_FILE), encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
# ---


def test():
    pass


if __name__ == '__main__':
    print(f'pid: {os.getpid()}')
    client = client.Client()
    tasks = []
    if config.DEBUG:
        tasks.append(
            client.loop.create_task(autoreboot.auto_reboot(client))
        )
    test()
    try:
        client.loop.run_until_complete(client.start(config.TOKEN))
    except KeyboardInterrupt as e:
        print(e)
    finally:
        for task in tasks:
            task.cancel()
        client.loop.run_until_complete(client.logout())
        client.loop.close()
