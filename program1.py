print("Welcome to Login/Signup Program")

ans = input("Do you have an account? please enter y/n:")

if ans == 'n':
    usr = input("Please Create Username: ")
    pas = input("Please Create Password: ")

    print("Congrulation, Your account created")

else:
    print("Please Login Here:")
    usrinput = input("Please Enter Your Username: ")
    pasinput = input("Please Enter Your Password: ")
    if usr == usrinput and pas == pasinput:
        print("Welcome to My World: ")

    else:
        print("Wrong username or Password")

