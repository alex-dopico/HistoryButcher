"""
stores well-known location for history files for different os's and browsers
    TODO: expand list with many more os' and browsers
    TODO: manage exceptions in get_os_user()
    TODO: automatize getting the login name, params: OS, browser
"""
from os_file_operations.get_os_info import get_current_user

current_user = get_current_user()

# OS & browser constants
OPERA_WIN_PATH = f'C:\\Users\\{current_user}\\AppData\\Roaming\\Opera Software\\Opera GX Stable\\History'
CHROME_WIN_PATH = f'C:\\Users\\{current_user}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History'
