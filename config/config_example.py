import os
import sys
from pathlib import Path

import objects.config.config_handler as ch

token = 'Your token here'
LOG_FILE = 'discord.log'
WORK_PATH = str(Path(os.path.dirname(os.path.abspath(__file__))).parents[0])
DEBUG = True
CONFIG_PATH = str(os.path.dirname(os.path.abspath(__file__)))

sys.modules[__name__] = ch.Config(globals())