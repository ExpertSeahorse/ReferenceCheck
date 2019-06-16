month= int(input("Please enter the number of the month: "))
oddOrEven = month % 2
if (month==2):
    print("There are 28 days in this month")
elif (oddOrEven == 0):
    print("There are 30 days in this month")
else:
    print ("There are 31 days in this month")