from AbstrClass import *
class PDFDocument(Document):
    def __init__(self):
        self.filename = ""
        self.file_size = 0
        self.msg = ""

    def open(self, filename):

        self.filename = filename
        self.file_size = 800
        self.msg = "This is a PDF document."
    def read(self):
        return self.msg

    def save(self, filename):
        print("The pdf document is saved!")
        pass
