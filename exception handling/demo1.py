def find_number():
    a=[1,2,4,5,6,6,7,89,6]
    try:
        print(a[12])

    except IndexError:
        print("Length Exceeded")  


find_number()          