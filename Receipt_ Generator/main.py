from itertools import count

while True:
    input1 = input("What's your item.. ")
    input2 = int(input("What's the price of your item.. "))
    n_input2 = list(count(input2))
    if len(n_input2) > 1:
        x = sum(n_input2)
        print(x)
        