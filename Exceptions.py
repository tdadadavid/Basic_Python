
from typing import final


try:
    with open("app.py") as file:
        print("App file opened")
    age = int(input("Age : "))
    xfactor = 10 / age
    print(xfactor)
except (ValueError, ZeroDivisionError) as exception:
    print("Enter a valid age ")
else:
    print("Excution continues")
