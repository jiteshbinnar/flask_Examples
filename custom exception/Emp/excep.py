class InvalidAgeError(Exception):


    def __init__(self, msg):
        self.msg=msg

class InvalidEmployeeIdError(Exception):
    def __init__(self,msg):
        self.note=msg


try:


    age=int(input('Enter age'))

    if age<18:



        raise InvalidAgeError("You are minor")

    else:

        print("you are eligible for voting")

except InvalidAgeError as i:
        print(i)  
      


