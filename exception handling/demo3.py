a=10;
try:
    print(10/0)

except IndexError:
    print("index out of bond")

except ZeroDivisionError:
    print("something wrong")

