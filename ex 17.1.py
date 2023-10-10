class Employee:
    __name = None
    __salary = None
    __age = None

    def __init__(self, name:str, salary:int, age:int):
        self.__name = name
        self.__salary = salary
        self.__age = age

    def getName(self):
        return self.__name
    def getSalary(self):
        return self.__salary
    def getAge(self):
        return self.__age

    def setName(self, name: str):
        self.__name = name
    def setSalary(self, salary: int):
        self.__salary = salary
    def setAge(self, age: int):
        self.__age = age

employee = Employee('Gosha', 1000000, 49)