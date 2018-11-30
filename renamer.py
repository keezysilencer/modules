import os
__author__ = 'Keezy Silencer'

"""
Renames files in a given directory to a preferred extension
"""


# OOP
class Rename:
    def __init__(self, to_ext, path):
        self.to_ext = to_ext
        self.path = path

    def rename(self):
        if self.to_ext[0] != '.':
            self.to_ext = '.' + self.to_ext
            print("Renaming files in {0}".format(self.path))
            for file_name in os.listdir(self.path):
                root, ext = os.path.splitext(file_name)
                print("Renaming: " + file_name + '  ==> ' + root + ext)
                os.rename(os.path.join(self.path, file_name), os.path.join(self.path, root + self.to_ext))

# Imperative programming
# def rename_by_ext(to_ext,path):
#     if to_ext[0]!='.':
#         to_ext = '.'+to_ext
#     print("Renaming files in ",path)
#     for file_name in os.listdir(path):
#         root,ext =os.path.splitext(file_name)
#         print("Renaming :"+file_name+' to '+root+ext)
#         os.rename(os.path.join(path,file_name),os.path.join(path,root+to_ext))
#
# rename_by_ext('.mp4','New Folder')

