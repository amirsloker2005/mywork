def digfill (num1 , num2):
    if len(num1) < len(num2):
        for i in range(len(num2) - len(num1)):
            num1 = "0" + num1
        return num1 , num2
    elif len(num2) < len(num1):
        for i in range(len(num1) - len(num2)):
            num2 = "0" + num2
        return num1, num2
    else:
        return num1, num2

def fintouch(num1):
    for i in range(len(num1)):
        if num1[i] == "1":
            num1 = num1[i:]
            break
    return num1
def firstcomp(num):
    z = str("")
    for i in range(len(num)):
        if num[i] == "0":
            z = z + "1"
        elif num[i] == "1":
            z = z + "0"
    return fintouch(z)

def secondcomp(num1):
    return fintouch(add(firstcomp(num1), "1", 1)[0])

def add(x, y, ad):
    num1 = digfill(x, y)[0]
    num2 = digfill(x, y)[1]
    carry = 0
    res = ""
    for i in range(-1,-(len(num1)+1),-1):
        if num1[i] == "0" and num2[i] == "0" and carry == 0:
            res = "0" + res
            carry = 0
        elif num1[i] == "0" and num2[i] == "1" and carry == 0:
            res = "1" + res
            carry = 0
        elif num1[i] == "1" and num2[i] == "0" and carry == 0:
            res = "1" + res
            carry = 0
        elif num1[i] == "1" and num2[i] == "1" and carry == 0:
            res = "0" + res
            carry = 1
        elif num1[i] == "1" and num2[i] == "1" and carry == 1:
            res = "1" + res
            carry = 1
        elif num1[i] == "0" and num2[i] == "1" and carry == 1:
            res = "0" + res
            carry = 1
        elif num1[i] == "1" and num2[i] == "0" and carry == 1:
            res = "0" + res
            carry = 1
        elif num1[i] == "0" and num2[i] == "0" and carry == 1:
            res = "1" + res
            carry = 0
    if carry and ad:
        res = "1" + res
    return fintouch(res), carry

def subtract(num1, num2):
    temp = digfill(num1,num2)
    x = add(temp[0], firstcomp(temp[1]), 0)
    if x[1] == 0:
        return fintouch(firstcomp(x[0]))
    elif x[1] == 1:
        return fintouch(add(x[0], "1", 1)[0])

def times(num1, num2):
    templist = []
    temp = 0
    for i in range(len(num2) -1 , -1, -1):
        if num2[i] == "1":
            templist.append(num1 + "0" * temp)
        else:
            templist.append("0")
        temp = temp + 1
    temp = "0"
    for i in range(len(templist)):
        temp = add(temp, templist[i], 1)[0]
    return fintouch(temp)

while True:
    print("**Binary Calculator**")
    print("A) Insert New Numbers")
    print("B) Exit")
    choose = input("")

    if choose == "A" or choose == "a":
        num1 = str(input("type number"))
        if any(digit not in {"0","1"} for digit in str(num1)):
            print("please enter a number within the allowed base")
            print("")
            continue
        print("**Please select the operation you want to make**")
        print("A) Compute one`s Complement")
        print("B) Compute Two`s Complement")
        print("C) Addition")
        print("D) Subtraction")
        print("E) Multiplication")
        choose = input("")
        if choose == "A" or choose == "a":
            print("The result is :", firstcomp(num1))
            continue
        elif choose == "B" or choose == "b":
            print("The result is :", secondcomp(num1))
            continue
        elif choose == "C" or choose == "c":
            print("type the second number for addition")
            num2 = str(input(""))
            if any(digit not in {"0","1"} for digit in str(num2)):
                print("please enter a number within the allowed base")
                print("")
                continue
            print("The result is:", add(num1, num2, 1)[0])
            continue
        elif choose == "D" or choose == "d":
            print("type the second number for subtraction")
            num2 = str(input(""))
            if any(digit not in {"0","1"} for digit in str(num2)):
                print("please enter a number within the allowed base")
                print("")
                continue
            print("The result is:", subtract(num1, num2))
            continue
        elif choose == "E" or choose == "e":
            print("type the second number for multiplication")
            num2 = str(input(""))
            if any(digit not in {"0","1"} for digit in str(num2)):
                print("please enter a number within the allowed base")
                print("")
                continue
            print("The result is:", times(num1, num2))
            continue
        else:
            print("Please enter a Valid Choice")
            continue
    if choose == "B" or choose == "b":
        break
    else:
        print("Please enter a Valid Choice")
        continue