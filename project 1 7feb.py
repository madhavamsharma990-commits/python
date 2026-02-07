class myclass :
    __privatevar = 27
    def __private_method(self):
        print("IM INSIDE CLASS myclass")
    def hello(self):
        print("private variable is ",myclass.__privatevar)
foo = myclass()
foo.hello()
##foo.__private_method()