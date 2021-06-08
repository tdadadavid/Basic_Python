class InvalidOperationError(Exception):
    pass


class Stream:
    def __init__(self):
        self.opened = False


    def open(self):
        if self.opened == True:
            raise InvalidOperationError("File already Opened")
        else:
            self.opened = True


    def close(self):
        if self.opened:
            raise InvalidOperationError("File is already closed")
        else:
            self.opened = False


    

class FileStream(Stream):
    print("Reading data from file")


class NetworkFile(Stream):
    print("Reading data from Network")