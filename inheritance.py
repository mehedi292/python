#parent class / super class
class Phone:
    def call(self):
        print("You can call")
    
    def message(self):
        print("You can message")
        
# child class / sub class
class Samsung(Phone):
    def photo(self):
        print("You can take photo")


s = Samsung()
s.message()
s.call()
s.photo()