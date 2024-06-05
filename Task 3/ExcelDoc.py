from AbstrClass import *
class ExcelDocument(Document):
    def __init__(self):
        self.filename = ""
        self.file_size = 0
        self.content = ""

    def open(self, filename):
        self.filename = filename
        self.file_size = 120
        self.msg = "This is an Excel document."

    def read(self):
        return self.msg

    def save(self, filename):
        print("The excel document is saved!")
        pass

