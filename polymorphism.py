# Built in polymorphic function
print(len("Mehedi Hasan"))
print(len([10,20,30,40,50]))

# user defined polymorphic function
def add(x,y,z=0):
    return x + y + z
print(add(2,5))
print(add(5,9,6))


# practice example
class India():
	def capital(self):
		print("New Delhi is the capital of India.")

	def language(self):
		print("Hindi is the most widely spoken language of India.")

	def type(self):
		print("India is a developing country.")

class USA():
	def capital(self):
		print("Washington, D.C. is the capital of USA.")

	def language(self):
		print("English is the primary language of USA.")

	def type(self):
		print("USA is a developed country.")

obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
	country.capital()
	country.language()
	country.type()

