# class one:
#     def __init__(self,name) -> None:
#         self.name=name
#         self.time=0
#     def work(self,time):
#         self.time=time-1

# class two(one):
#     def __init__(self, name,time):
#         self.time=time+1
#         self.work(time)
#         # super().__init__(name)

# d=two("Mike",2)
# print(d.time)
# # print(d.name)

class A:
	def init(self, n='Rahul'):
		self.name = n

class B:
	def __init__(self, roll):
		self.roll = roll
    def rie(self, name):
        self.name=name

# object = B(23)
# print(object.name)
