usrList = []
pasList = []
print("Welcome to Login/Signup Program")

ans = input("Do you have an account? please enter y/n:")

if ans == 'n':
    usr = input("Please Create Username: ")
    usrList.append(usr)
    pas = input("Please Create Password: ")
    pasList.append(pas)
    print("Congrulation, Your account created")

else:
    print("Please Login Here:")
    usrinput = input("Please Enter Your Username: ")
    pasinput = input("Please Enter Your Password: ")
    if usrinput == (usrList) and pasinput == (pasList):
        print("Welcome to My World: ")

    else:
        print("Wrong username or Password")

