
try:
    age = int(input("Age : "))
    xfactor = 10 / age
    print(xfactor)
except (ValueError, ZeroDivisionError) as exception:
    print("Enter a valid age ")
else:
    print("Excution continues")
