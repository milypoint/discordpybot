import logging
import os
import sys
from config.config_handler import Config
from bot_tasks import autoreboot
if 'client' in sys.modules:
    client = sys.modules['client']
else:
    import client

# Setting logger:
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename=os.path.join(os.getcwd(), Config().LOG_FILE), encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
# ---


if __name__ == '__main__':
    client = client.Client()
    config = Config()
    if config.DEBUG:
        client.loop.create_task(autoreboot.auto_reboot(client))
    # Main loop:
    client.run(config.token)
