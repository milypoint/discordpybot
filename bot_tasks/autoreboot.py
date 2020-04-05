import asyncio
import os

from config import config


def get_py_files(root):
    """returns list of all files with *.py extensions as full path"""
    path_list = []
    for p in os.listdir(root):
        if os.path.isfile(os.path.join(root, p)) and p[-3:] == '.py':
            path_list.append(os.path.join(root, p))
        elif os.path.isdir(os.path.join(root, p)):
            for _p in get_py_files(os.path.join(root, p)):
                path_list.append(_p)
    return path_list


async def auto_reboot(client):
    """Restart the current program"""
    def mtime_files(fl):
        mtimes = list()
        for file in fl:
            mtimes.append(os.stat(file).st_mtime)
        return max(mtimes)

    await client.wait_until_ready()
    files = get_py_files(config.WORK_PATH)
    last_time = mtime_files(files)

    while (True):
        if mtime_files(files) > last_time:
            await client.logout()
        await asyncio.sleep(1)
