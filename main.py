# from invoke import task
import threading
import sys
import subprocess


class Update:
    __instance = None
    __lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        with cls.__lock:
            if cls.__instance is None:
                cls.__instance = super().__new__()
        return cls.__instance

    def __init__(self):
        self.path = ""
        # self.repo = git.Repo(path)

    def __str__(self):
        return self.path

    def __repr__(self):
        return self.path

    def register(self):
        import winreg

        # Define the registry key path
        key_path = r"directory\shell\myCustomKey\command"

        # Open the registry key for writing
        key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, key_path)

        # Set the command to execute when the context menu option is clicked
        command = r'%PYTHONPATH% "F:\Projects\Python\autoupdate\script.py" %1'
        winreg.SetValueEx(key, None, 0, winreg.REG_EXPAND_SZ, command)

        # Close the key
        if key:
            winreg.CloseKey(key)

    def update(self):
        path = self._get_paths()
        try:
            subprocess.run(['git', "add", "."], cwd=path, shell=True)
            subprocess.run(['git', "commit", "-m", "update"], cwd=path, shell=True)
            subprocess.run(['git', "push", "origin", "master"], cwd=path, shell=True)
        except subprocess.CalledProcessError:
            print("git add error")

    def _get_paths(self):
        if len(sys.argv) > 1:
            self.path = " ".join(sys.argv[1:]).encode("utf-8").decode("utf-8")
        else:
            print("Path is not found")
        return self.path


# @task
# def update(ctx):
#     # update = Update()
#     # update.register()
#     # update.update()
#     ctx.run("start google.com")