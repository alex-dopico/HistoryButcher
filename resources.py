"""
stores well-known location for history files for different os's and browsers,
also builds destination path string build of user_name+date+historial
    TODO: expand list with many more os' and browsers
    TODO: manage exceptions in get_os_user()
    TODO: automatize getting the login name, params: OS, browser
"""
from datetime import date
import getpass
import platform
import pathlib


current_os = platform.platform()
current_user = getpass.getuser()
current_date = date.today()

# OS & browser constants
OPERA_WIN_PATH = pathlib.Path(f'C:\\Users\\{current_user}\\AppData\\Roaming\\Opera Software\\Opera GX Stable\\History')
CHROME_WIN_PATH = pathlib.Path(f'C:\\Users\\{current_user}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History')

# destination path
DESTINATION = pathlib.Path(f'C:\\Users\\{current_user}\\Documents\\HistoryButcher\\{current_user}{current_date}_historial')


def get_browser_path():
    if current_os.startswith('Windows'):
        return OPERA_WIN_PATH
