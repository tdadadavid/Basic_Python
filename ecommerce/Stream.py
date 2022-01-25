from abc import ABC, abstractmethod


class InvalidOperationError(Exception):
    pass


class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened == True:
            raise InvalidOperationError("File already Opened")
        else:
            self.opened = True
            print("Opened")

    def close(self):
        if self.opened:
            raise InvalidOperationError("File is already closed")
        else:
            self.opened = False

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from file")


class NetworkFile(Stream):
    def read(self):
        print("Reading data from Network")


class MemmoryStream(Stream):
    def read(self):
        print("Reading file from Memmory!")


newStream = MemmoryStream()
newStream.open()
