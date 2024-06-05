
from AbstrClass import *
from WordDOC import *
from PDFDoc import *
from ExcelDoc import *
from AbstrFact import *

if __name__ == "__main__":
    factory = DocumentFactory()

    doc_1 = factory.create_document("Word")
    doc_1.open("example.docx")
    print("This is my Final Code, yay!.", doc_1.read())

    doc_2 = factory.create_document("PDF")
    doc_2.open("example.pdf")
    print("This is my Final Code, yay!.", doc_2.read())

    doc_3 = factory.create_document("Excel")
    doc_3.open("example.xlsx")
    print("This is my Final Code, yay!.", doc_3.read())
