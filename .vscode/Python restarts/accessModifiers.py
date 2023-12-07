class Emp:
    def __init__(self) -> None:
        self.name="ritik"
        self.__name="jain"
    

a=Emp()
print(a.name)
# print(a.__name)
print(a._Emp__name)