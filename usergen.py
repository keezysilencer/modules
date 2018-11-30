import string, secrets, xlrd

"""
Generates random password of 32 chars long
and maps user to a password and returns a dictionary.
"""


class UserGen():
    def __init__(self, path):
        self.path = path
        self.pack = []


#    Reads file from an excel file and returns a list of usernames

    def read(self):
        book = xlrd.open_workbook(self.path)
        sheet = book.sheet_by_index(0)
        columns = sheet.ncols
        row = sheet.nrows
        print("You have " + str(row) + " rows" + ' and ' + str(columns) + ' column' + ' in ' + sheet.name)
        ID,last,first = [],[],[]
        for r in range(1, row):
            ID.append(sheet.cell(r, 0).value)
            first.append(sheet.cell(r, 1).value)
            last.append(sheet.cell(r, 2).value)
            self.pack_id = ID
        return self.pack_id
    #Find list of emails on column 5 (E)
    def email_list(self):
        book = xlrd.open_workbook(self.path)
        sheet = book.sheet_by_index(0)
        row = sheet.nrows
        self.email = []
        for r in range(1, row):
            self.email.append(sheet.cell(r,4).value)
        return self.email
    # returns a string of 32 chars of random letters and digits
    def gen(self):
        words = string.ascii_letters + string.digits
        text = ''.join(secrets.choice(words) for _ in range(5))
        return text

    # remove duplicates from generated file
    def collect(self):
        collection = []
        for _ in range(len(self.pack_id)):
            word = self.gen()
            collection.append(word)
        collection = set(collection)
        collection = list(collection)
        return collection
