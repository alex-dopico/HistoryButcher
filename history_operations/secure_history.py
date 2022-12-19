"""
Copia el historial de navegacion con el nombre cambiado a fecha actual
"""
import shutil
import time
import resources
from os import error


def secure_user_history():
    try:
        # retrieves appropriate path to history
        path = resources.CHROME_WIN_PATH

        # formats a time string
        today = time.strftime("_%Y_%m_%d")

        # shutil copies db file from browser path to local path
        src_history_path = path
        dst_history_path = f'{resources.get_os_user()}{today}_history'
        shutil.copy(src_history_path, dst_history_path)

        # if ok
        print('Successfully secured')
        return True

    except error as e:
        print('Not possible to secure history file. Run. Now.')
        print(e)
        return False
