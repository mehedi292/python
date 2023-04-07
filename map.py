def square(x):
    return x*x
num = [1,2,3,4,5]

result = list(map(square,num))
print(result)



# map lambda
num=[1,2,3,4,5,6,7,8,9,10]
result = list(filter(lambda x: x%2==0,num))
print(result)


# map list
num =[1,2,3,4,5]
result = list(map(lambda x: x*x, num))
print(result)


# comprehansion map list
num =[1,2,3,4,5]
result = [x*x for x in num] # expression for item in list
print(result)