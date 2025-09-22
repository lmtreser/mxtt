from debug import debug

class MXTTFile:

    def __init__(self, filename="config.json"):
        self.file = open(filename, "a+")

    def write(self, data):
        self.file.write(data)
        debug(f"Data written to file: {data}")

    def read(self):
        self.file.seek(0)
        data = self.file.read()
        debug(f"Data read from file: {data}")
        return data
    
hello = MXTTFile()
data = hello.read()
print(data)