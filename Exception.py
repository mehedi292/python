
try:
    num1= int(input("Enter 1st number: "))
    num2= int(input("Enter 2nd number: "))
    result = num1/num2
    print(result)
    # list = [5,0,20]
    # result = list[0]/list[2]
    # print(result)

except ValueError:
    print("You have to insert only integer ")

except ZeroDivisionError: 
    print("division by zero")

except IndexError:
    print("Index error")

finally:
    print ("Greatful")
print("successful")

# vote example
def voter (age):
    if age < 18:
        