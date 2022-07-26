age=int(input("Enter the age"))
if age>18:
    print("Can take vaccine")
    Vaccinated=input("Enter yes or no")
    if Vaccinated=="yes":
        print("Go for 2nd dose")
    else:
        print("Go for 1st dose")

else:
    print("can't take vaccine")
       