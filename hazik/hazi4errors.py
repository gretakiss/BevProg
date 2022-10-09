def osztas(a,b):
    try:
        eredmeny = a / b
        print(round(eredmeny,1))

    except ZeroDivisionError:
        print("Divison by zero not allowed")

    finally:
        print('Out of try except blocks')

while True:
    a = float(input("Enter 'a' value: "))
    b = float(input("Enter 'b' value: "))
    osztas(a,b)