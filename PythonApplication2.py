import sys

class UserInfo(object):
    
    #initializes class variables
    def __init__(self):
        self.username = ""
        self.age = 0
        self.userid = 0

    #Gracefully closes application by typing exit in any prompt
    def check_input(self):
        Exit_List = ["exit", "Exit", "EXit", "EXIt", "EXIT", "exIT", "eXIT"]

        if self.username in Exit_List:
            exit(0)
        elif self.age in Exit_List:
            exit(0)
        elif self.userid in Exit_List:
            exit(0)
        elif self.username == "":
            print("Field can not be left blank")
            self.get_username()
        elif self.age == "":
            print("Field can not be left blank")
            self.get_age()
        elif self.userid == "":
            print("Field can not be left blank")
            self.get_userid()

    #Checks if input is a number for age and userid
    def is_number(self, test):
        try:
            int(test)
            return True
        except ValueError:
            return False

    #Checks if input is above 1 and makes sure integers are inputed
    def is_possitive(self, num):
        try:
            if num == self.age:
                if int(self.age) < 1:
                    print("Please enter a possitive integer above 1")
                    self.get_age()
            if num == self.userid:
                if int(self.userid) < 1:
                    print("Please enter a possitive integer above 1")
                    self.userid
        except ValueError:
            if num == self.age:
                print("Please enter a valid age (1-85)")
                self.get_age()
            elif num == self.userid:
                print("Please enter a valid ID (1-999999)")
                self.get_userid()


    #Checks if input is in desired range 1-999999
    def in_range(self, num):
        if num == self.age:
            if int(num) < 1 or int(num) > 85:
                print("Please enter a valid age (1-85)")
                self.get_age()
        elif num == self.userid:
            if int(num) < 1 or int(num) > 9999999:
                print("Please enter a valid ID (1-999999)")
                self.get_userid()


    #Gets input from user for username
    def get_username(self):
        self.username = input("Please enter your username: ")
        self.check_input()
        return self.username

    #Gets input from user for age
    def get_age(self):
        self.age = input("Please enter your age (1-85): ")
        self.check_input()
        self.is_possitive(self.age)
        self.in_range(self.age)
        return self.age

    #Gets input from user for userid
    def get_userid(self):
        self.userid = input("Please enter your userID (1-999999): ")
        self.check_input()
        self.is_possitive(self.userid)
        self.in_range(self.userid)
        return self.userid

#Create a new instance of UserInfo Class
user_report = UserInfo()


#Save the user_report.username() data to variable "name"
#Makes user input a string and not a number
try:
    name = int(user_report.get_username())
    while name == int(user_report.username):
        print("Please do not use numbers")
        name = int(user_report.get_username())
except ValueError:
    name = user_report.username

#Save the user_report.age() data to variable "age"
#Checks if user input is_number()
if user_report.is_number(user_report.get_age()) == True:
    age = int(user_report.age)
else:
    print("Please enter a valid age (1-85)")
    while user_report.is_number(user_report.get_age()) == False:
        print("Please enter a valid age (1-85)")
    else:
        age = int(user_report.age)


#Save the user_report.userid() data to variable "userid"
#Checks if user input is_number()
if user_report.is_number(user_report.get_userid()) == True:
    userid = int(user_report.userid)
else:
    print("Please enter a valid ID (1-999999)")
    while user_report.is_number(user_report.get_userid()) == False:
        print("Please enter a valid ID (1-999999)")
    else:
        userid = int(user_report.userid)

print("You are %s, aged %s, next year you will be %s, with a user id %s, the next user id is %s." % (name,
                                                                                                     age,
                                                                                                     age + 1,
                                                                                                     userid,
                                                                                                     userid + 1))