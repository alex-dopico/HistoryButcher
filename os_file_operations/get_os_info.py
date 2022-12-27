"""
Script file to retrieve everything necessary from the os
"""

import getpass
import platform
from platform import *


def get_current_user():
    current_user = getpass.getuser()
    return current_user


def get_current_os():
    current_os = platform.platform()
    return current_os
