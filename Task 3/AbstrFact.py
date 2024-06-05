from AbstrClass import *
from WordDOC import *
from PDFDoc import *
from ExcelDoc import *
class DocumentFactory:
    @staticmethod
    def create_document(doc_type):
        if doc_type == "Word":
            return WordDocument()
        elif doc_type == "PDF":
            return PDFDocument()
        elif doc_type == "Excel":
            return ExcelDocument()
        else:
            raise ValueError("Invalid document type")

