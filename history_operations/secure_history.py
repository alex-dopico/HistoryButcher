"""
Copia el historial de navegacion con el nombre cambiado a fecha actual
"""
import shutil
import resources
from os import error


def secure_user_history():
    try:
        # retrieves appropriate path to history
        history_path = resources.get_browser_path()
        destination_path = resources.DESTINATION

        # shutil copies db file from browser path to local path
        shutil.copyfile(history_path, destination_path)

        # if ok
        print('Successfully secured')
        return True

    except error as e:
        print('Not possible to secure history file. Run. Now.')
        print(e)
        return False
