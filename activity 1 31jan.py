class IOstring():
    def __init__(self):
        self.strl = ""
    def get__string(self):
        self.strl = input("Enter a string: ")
    def print__string(self):
        print("Result is :", self.strl.upper())
str1 = IOstring()
str1.get__string()
str1.print__string()