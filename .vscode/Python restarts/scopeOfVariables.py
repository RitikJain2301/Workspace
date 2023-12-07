class A:

    name="Ritik"

    def __init__(self) -> None:
        self.name="Junkie"

    @classmethod
    def ins (self):
        # global name
        self.name="Jain"

var=A()             # ==>  instance created
var.ins()           # ==>  name variable assigned to the instance
print(var.name)     # ==>  print name inside the method
print(A.name)
 