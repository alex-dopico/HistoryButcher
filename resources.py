"""
stores well-known location for history files for different os's and browsers
    TODO: expand list with many more os' and browsers
    TODO: manage exceptions in get_os_user()
    TODO: automatize getting the login name, params: OS, browser
"""
import getpass


def get_os_user():
    current_user = getpass.getuser()
    return current_user


OPERA_WIN_PATH = f'C:\\Users\\{get_os_user()}\\AppData\\Roaming\\Opera Software\\Opera GX Stable\\History'
CHROME_WIN_PATH = f'C:\\Users\\{get_os_user()}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History'
