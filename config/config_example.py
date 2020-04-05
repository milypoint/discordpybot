import os
from pathlib import Path

token = 'Your token here'
LOG_FILE = 'discord.log'
WORK_PATH = str(Path(os.path.dirname(os.path.abspath(__file__))).parents[0])
DEBUG = True
