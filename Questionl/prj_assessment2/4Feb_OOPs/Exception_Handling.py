try:
    x = int(input("Enter the number"))
    y = int(input("Enter the number"))
    print(x/y)
except ZeroDivisionError:
    print("Error")
except ValueError:
    print("value error")
    