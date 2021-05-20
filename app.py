# Practicing logical operaors
# and , or , not

high_income = False
good_credit = True
student = False

if high_income and good_credit:
    print("Eligible")
else:
    print("Not Eligible")

# Output = not Eligble


if high_income or good_credit:
    print("Eligible")
else:
    print("Not Eligible")

# output  = Eligible

if high_income or good_credit and not student:
    print("Eligible")
else:
    print("Not Eligible")
