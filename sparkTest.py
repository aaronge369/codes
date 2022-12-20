import json

class DepartmentEmployee:
    def __init__(self, name: str = '', salary: str = "0"):
        self.name = name
        self.salary = salary

    def to_json(self):
        return json.dumps(self.__dict__)

    def dicc(self):
        return self.__dict__

E1 = DepartmentEmployee('Tom', 123)
print(E1.to_json())
print(E1.dicc())
