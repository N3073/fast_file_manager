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
    _clipboard     = set()
    _current_path  = Path("/.")
    _current_items = []
    def __init__(self,spawn_path:str="~"):
        self.set_current_path(Path(spawn_path))


    def set_current_path(self,path:Path):
        if path.exists() and path.is_dir():
            self._current_path = path
            self.list_contents()

    def list_contents(self):
        if self._current_path.exists() and self._current_path.is_dir():
            folder_items = list(self._current_path.iterdir())
            child_folders = list(filter(lambda x : x.is_dir(),folder_items))
            child_files = list(filter(lambda x : x.is_file(),folder_items))
            self._current_items = child_folders+child_files
        else:
            self._current_items = []

    def get_contents(self):
        return self._current_items

    def add_to_clipboard(self,item):
        self._clipboard.add(item)

    def list_clipboard(self):
        return sorted(list(self._clipboard))

    def get_current_path(self):
        return self._current_path
