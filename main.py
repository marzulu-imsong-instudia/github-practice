print('Hello World')
def add(a, b):
<<<<<<< HEAD
    if not (a%2==0 or b%2==0):
        sum = a + b
        print(f"Sum of {a} and {b} :{sum}")
    else:
        print("This function only adds odd numbers")
=======
    if a%2==0 and b%2==0:
        sum = a + b
        print(f"Sum of {a} and {b} :{sum}")
    else:
        print("This function only adds even numbers")
>>>>>>> 4935219 (feat: added a condition to add only even numbers)
add(1, 5)
