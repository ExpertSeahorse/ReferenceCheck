def add(n1, n2):
    return n1 + n2


num1 = 10
num2 = "Dipshit"
try:
    a = add(num1, num2)
except:
    print("Hey it looks like youre dumb")
else:
    print('add went well')
    print(a)
print("My parents love me")


#######################################################################################################################
try:
    f = open('testfile', 'r')
    f.write("This is a test")
except TypeError:
    print("There was a Type Error")
except OSError:
    print("Hey you have an I/O Error")
finally:
    print("I always run")


def ask_for_int():
    while True:
        try:
            result = int(input("Please provide number"))
        except:
            print("Whooops! Youre dumb")
            continue
        else:
            print("Thanks")
            break
        #finally:                                       Dont use finally with else even tho you can
        #    print("End of try/except/finally")


ask_for_int()