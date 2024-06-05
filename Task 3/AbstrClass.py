from abc import ABC, abstractmethod


# Document Interface
class Document(ABC):
    @abstractmethod
    def open(self, filename):
        pass

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def save(self, filename):
        pass