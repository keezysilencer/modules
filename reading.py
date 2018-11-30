import xlrd

"""
Reads file from an excel file and returns a list
"""
#OOP
class Read():
    def __init__(self, path):
        self.path = path
        self.pack = []

    # read data from excel file
    def read(self):
        book = xlrd.open_workbook(self.path)
        sheet = book.sheet_by_index(0)
        columns = sheet.ncols
        row = sheet.nrows
        print("You have " + str(row) + " rows" + ' and ' + str(columns) + ' column' + ' in ' + sheet.name)
        ID = []
        first = []
        last = []
        for r in range(1, row):
            ID.append(sheet.cell(r, 0).value)
            first.append(sheet.cell(r, 1).value)
            last.append(sheet.cell(r, 2).value)
            self.pack_id= ID
        return self.pack_id


# Mc = Read(path='uewtest.xlsx')
# print(Mc.read())


#Imperative programming
# book = xlrd.open_workbook("uewtest.xlsx")
# sheet =  book.sheet_by_index(0)
#
# columns = sheet.ncols
# row = sheet.nrows
# print(row,columns)
# print("You have "+str(row)+" rows"+ ' and '+str(columns)+' columns'+ ' in '+ sheet.name)
# ID = []
# first = []
# last = []
# for r in range(1, row):
#     ID.append(sheet.cell(r,0).value)
#     first.append(sheet.cell(r,1).value)
#     last.append(sheet.cell(r,2).value)
# user = dict(zip(ID,first))
# print(user)
