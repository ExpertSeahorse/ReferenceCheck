def menu ():
    print("Choices are:\t\t1- convert to yards\n" +
          "\t\t\t\t\t2 - convert to inches\n" +
          "\t\t\t\t\t3 - convert to feet")
    return


def yard(n):
    return n * 1.09361


def inches(n):
    return n * 39.3701


def feet(n):
    return n * 3.28084


q = "yes"
while q != "no":

    # Choosing inputs and validating if correct
    print("\nThis is a program to convert meters into another unit")
    menu()

    print("What is your choice?")
    ch=int(input())
    while ch < 1 or ch > 3:
        print("Try again:")
        ch = int(input())

    print("Enter the distance in meters: ")
    d = float(input())
    while d < 0:
        print("Try again:")
        d = float(input())

    if ch == 1:
        print(str(d)+" meters is "+str(yard(d))+" yards.")
    elif ch == 2:
        print(str(d)+" meters is "+str(inches(d))+" inches.")
    elif ch == 3:
        print(str(d)+" meters is "+str(feet(d))+" feet.")

    print("Do you want to continue?(type \"no\" to quit)")
    q = str(input())
print("Have a great day :)")