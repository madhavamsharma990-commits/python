class Employee:
    def __init__(self):
        print("Employee created")
    def __del__(self):
        print("Destructor called")
def create_object():
     print('making object...')
     object = Employee()
     print('function end...')
     return object
print("calling create_object() function...")
object = create_object()
print("program end...")