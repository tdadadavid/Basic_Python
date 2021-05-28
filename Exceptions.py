from timeit import timeit


code1 = """
def calc_xfactor(age):
    if age <= 0:
        raise ValueError("Age must not be 0 or less")
    retrun 10 / age



try:
    calc_xfactor(2)
except ValueError as error:
    print(error)
"""
print("Firstcode ", timeit(code1, number=1000))
