from base_command import ICommand
import os
import subprocess
import winreg
import sys

class Update(ICommand):

    def update_git(self, path):
        try:
            # check if it is a git repository
            if os.path.join(path, '.git'):
                # check if the repository is clean
                if subprocess.call(['git', 'diff-index', '--quiet', 'HEAD', '--']) != 0:
                    # add all files
                    subprocess.call(['git', 'add', '.'])
                    # push the repo
                    subprocess.call(['git', 'push'])
                else:
                    print("No changes to push")
        except:
            pass




    def get_path(self):
        pass

    def execute(self):
        print("Update")