temperature = 30

if temperature > 50:
    print("Really Hot!")
    print("Have a cold bath")
else:
    print("The temperature is okay!")

# Using the tenary oprator to write
# the same logic we have

message = "Really hot " and "Have a cold bath" if temperature > 50 else "The temperature is okay!"
print(message)
