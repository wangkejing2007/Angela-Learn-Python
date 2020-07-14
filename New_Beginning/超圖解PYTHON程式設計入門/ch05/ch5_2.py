# ：參閱5-17頁

import os
from os import path
import platform


def pyTube_folder():
    sys = platform.system()
    home = path.expanduser('~')

    if sys == 'Windows':
        folder = path.join(home, 'Videos', 'PyTube')
    elif sys == 'Darwin':
        folder = path.join(home, 'Movies', 'PyTube')

    if not os.path.isdir(folder):  # 若'PyTube'資料夾不存在…
        os.mkdir(folder)           # 則新增資料夾

    return folder
