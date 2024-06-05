from AbstrClass import *
class WordDocument(Document):
    def __init__(self):
        self.filename = ""
        self.file_size = 0
        self.msg = ""

    def open(self, filename):
        self.filename = filename
        self.file_size = 120
        self.msg = "This is a Word document."

    def read(self):
        return self.msg

    def save(self, filename):
        print("The word document is saved!")
        pass

