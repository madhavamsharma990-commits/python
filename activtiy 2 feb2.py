class person:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def display(self):
        print("Name:", self.name)
        print("ID:", self.id)
class employee(person):
    def __init__(self, name, id, salary, post):
        super().__init__(name, id)
        self.salary = salary
        self.post = post
    def display_employee(self):
        self.display()
        print("Salary:", self.salary)
        print("Post:", self.post)
object = employee("John", 101, 50000, "Manager")
object.display()