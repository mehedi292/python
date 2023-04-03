# addition
def add(a, b, c):
    sum = a+b+c
    print(sum)


add(20, 30, 90)
add(50, 50, 80)
add(20, 20, 60)


# submission
def sub(x, y):
    result = x-y
    print(result)


sub(52, 12)


# no parameter
def message():
    print("No Parameter")


message()


# example
def add(a, b):
    sum = a+b
    return sum


result = add(20, 30)
print("Result = ", result)


# large number check

def large(a, b):
    if a > b:
        return a
    else:
        return b


print(large(100, 200))
