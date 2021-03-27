def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def subtract(a, b):
    return a - b


def divide(a, b):
    return a / b


print("1.add")
print("2.multiply")
print("3.subtract")
print("4.divide")
while True:
    ch = input("enter the operator")
    if ch in ('1', '2', '3', '4'):
        n1 = float(input())
        n2 = float(input())
        if ch == '1':
            print(add(n1, n2))
        elif ch == '2':
            print(multiply(n1, n2))
        elif ch == '3':
            print(subtract(n1, n2))
        elif ch == '4':
            print(divide(n1, n2))
        break
    else:
        print('enter valid value')
