import sys
import time

import objects.client as client


def guild():
    if not hasattr(client, 'Client'):
        return

    cl = client.Client()

    try:
        return cl.guilds[0]
    except IndexError as e:
        print('Client don`t have guilds.')
        return


def channel_by_id(_id, ch_type=None):
    server = guild()
    if server is None:
        return
    try:
        ch = [ch for ch in server.channels if ch.id == _id][0]
        return ch if ((ch_type is None) or isinstance(ch, ch_type)) else None
    except IndexError as e:
        print('Server don`t have VoiceChannel')
