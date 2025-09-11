from pylint import interfaces
from pathlib import Path
import os, shutil
from shutil import move

class FileTreeNavigator():
    """
    A class encapsulating the filemanager logic we want to use via the pyqt interfaces.

    This class creates an abstraction layer between the intricate file manager logic and the GUI.
    This class has the ability to save file path to a virtual clipboard from multiple source folders
    and drop these files off to a single or multiple locations.
    This is the primary functionality of this class. To be able to pick items up along the way and drop
    them where ever the user wants to.

    """
    _clipboard = set()
    _current_path = Path("/.")
    def __init__(self,spawn_path:str="~"):

    def navigate_to(self,):
        pass
    def set_current_path(self,path:str):
        new_path = Path(path)
        if new_path.exists() and
        pass
