import random

firstNum = random.randrange(0 , 3)
secondNum = random.randrange(2,29)

print("what is the sum of the two numbers")
print(f"Num1: {firstNum }")
print(f"Num2: {secondNum}")

userInput = eval(input("Ans:"))

if userInput :
    print("Correct")
else:
    print("Wrong!!")
    



# print("Enter two numbers of your choice")

# input1 = eval(input("Num1: "))
# input2 = eval(input("Num2: "))

# sum = input1 + input2

# print(sum)