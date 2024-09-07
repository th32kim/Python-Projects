


# def add(*numbers):
#     sum = 0
#     for n in numbers:
#         sum +=n
#     return sum

# print(add(1,2,3,4,5,6,7,8,9))

def calculate(n,**kwarg):
    n+=kwarg["add"]
    n*=kwarg["multiply"]
    print(n)


calculate(2,add=3,multiply=5)