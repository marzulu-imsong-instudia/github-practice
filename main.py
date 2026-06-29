print('Hello World')
def add(a, b):
    if not (a%2==0 or b%2==0):
        sum = a + b
        print(f"Sum of {a} and {b} :{sum}")
    else:
        print("This function only adds odd numbers")
add(1, 5)
