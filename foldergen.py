import os
import secrets
import string

__author__ = "Keezy Silencer"
"""
 Creates unlimited number of folders in the current directory
"""


class Maker:
    def __init__(self, num):
        self.num = num

    # #this creates dir of the specified number in n with each dir 5 characters.
    def create(self):
        fname = []
        for __ in range(int(self.num)):
            words = string.ascii_letters + string.digits
            text = ''.join(secrets.choice(words) for _ in range(5))
            fname.append(text)
        for k in range(len(fname)):
            os.mkdir(fname[k])
        print("+++++++++++++ Done ++++++++++!\n" + str(self.num) + ' FILES CREATED!')
        return None


#folder = Maker("20")
#folder.create()
