import secrets
import string
import xlrd

"""
Generates random password of 32 chars long
and maps user to a password and returns a dictionary.
"""


class UserGen:
    pack_id = []
    email = []

    def __init__(self, path):
        self.path = path

    def read(self):
        """
         Reads file from an excel file and returns a list of username
        """
        book = xlrd.open_workbook(self.path)
        sheet = book.sheet_by_index(0)
        columns = sheet.ncols
        row = sheet.nrows
        print("You have " + str(row) + " rows" + ' and ' + str(columns) + ' column' + ' in ' + sheet.name)
        last, first = [], [],
        for data in range(1, row):
            first.append(sheet.cell(data, 1).value)
            last.append(sheet.cell(data, 2).value)
            self.pack_id.append(sheet.cell(data, 0).value)
        return self.pack_id

    def email_list(self):
        """
        Find list of emails on column 5 (E)
        """
        book = xlrd.open_workbook(self.path)
        sheet = book.sheet_by_index(0)
        row = sheet.nrows
        self.email = []
        for r in range(1, row):
            self.email.append(sheet.cell(r, 4).value)
        return self.email

    @staticmethod
    def gen():
        """
        returns a string of 32 chars of random letters and digits
        """
        words = string.ascii_letters + string.digits
        text = ''.join(secrets.choice(words) for _ in range(5))
        return text

    def collect(self):
        """
        remove duplicates from generated file
        """
        collection = []
        for _ in range(len(self.pack_id)):
            word = self.gen()
            collection.append(word)
        collection = set(collection)
        collection = list(collection)
        return collection
