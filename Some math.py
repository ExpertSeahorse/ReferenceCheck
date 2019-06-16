import string


def lowhi(num, low, high):
    return low <= num <= high


def cap(s):
    caps= 0
    lower= 0
    for i in s:
        if i in string.ascii_uppercase:
            caps += 1
        elif i in string.ascii_lowercase:
            lower += 1
    print("Uppercase Letters: ", caps)
    print("Lowercase Letters: ", lower)


def unique_list(x):
    return set(x)


def multiply(y):
    mult=1
    for i in y:
        mult *= i
    return mult


def palin(z):
    x = list(z)
    y = x[::-1]
    index = 0
    for letter in list(x):
        if letter == y[index]:
            index += 1
            continue
        else:
            return False
    return True


def pangram(s1, alph= string.ascii_lowercase):
    alphaset = set(alph)
    return alphaset <= set(s1.lower())


mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = list(map(lambda rad: (4.0/3) * rad**3 * 3.14, mylist))
print(a)

# bee= str(input("What phrase?"))
cap("What is the word of God Pastor Rodger?")

slist = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 5]
print("Shortened slist: ", unique_list(slist))

print(multiply(mylist))

p= "racecar"
print("Is ", p, " a palindrome: ", palin(p))

q= "the quick brown fox jumps ove the lazy dog"
print("Is ", q, " a pangram: ", pangram(q))

