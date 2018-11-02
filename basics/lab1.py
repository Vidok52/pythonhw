#First task:
def printer(str1):
    print(str1)

printer("Hello, %arg%!")

#Second task
def sum(list1):
    result = 0
    for i in list1:
        result = result + i
    print(result)

def multiply(list1):
    result = 1
    for i in list1:
        result = result * i
    print(result)

rand = [1,2,3,4,5,6]

sum(rand)
multiply(rand)

#Third task:

a = "Anton"

def reverse(str1):
    count = len(str1)
    count = count+1
    i = 1
    while i < count:
        print(str1[-i])
        i += 1

reverse("Anton")

#Fourth task:

def isPalindrome(str1):
    count= len(str1)
    count = count+1
    i=1
    palindrome = ""
    while i < count:
        palindrome += str1[-i]
        i += 1
    if palindrome == str1:
        print("True")
    else:
        print("False")
    

isPalindrome("rar")
isPalindrome("Anton")

#Fifth task:

def histogram(lst1):
    for i in lst1:
        count = 0
        result = ""
        while count < i:
            count +=1
            result = result + "=##= "
        print(result)

       
histogram([1,2,3,4])

# Sixth task:

def caesarCipher(str1, key=2):
    print ("As was: ",str1)
    ChipStr1 = ""
    for i in str1:
        num1 = ord(i)
        chr1 = chr(num1 + key)
        ChipStr1 = ChipStr1 + chr1
    print ("As is: ", ChipStr1)

caesarCipher("Tony")     

# Seventh task:

import random

def diagonalReverse(row,col):
    matrix = [[random.randrange(0,10) for i in range(row)] for z in range(col)]
    print("As was:")
    for z in range(len(matrix)):
        print(matrix[z])
    print("As is:")
    # First change
    a = (matrix[0])
    b = (matrix[1])
    buf = a[1]
    a[1] = b[0]
    b[0] = buf
    # Second change
    a = (matrix[0])
    b = (matrix[2])
    buf = a[2]
    a[2] = b[0]
    b[0] = buf
    # Third change
    a = (matrix[1])
    b = (matrix[2])
    buf = a[2]
    a[2] = b[1]
    b[1] = buf
    for z in range(len(matrix)):
        print(matrix[z])
   
    

diagonalReverse(3,3)

# Eights task:

def game(arg1, arg2):
    a = random.randrange(arg1,arg2)
    b = input("Please input you digit:")
    while a !=  b:
        print("Try again")
        b = input("Please input you digit:")
    print("You got it!")

game(1,2)

# Ninth task:

def br(arg1):
    counter = 0
    length = len(arg1)    
    for i in range(length):
        if counter < 0:
            print("Its not ok")
            break
        else:
            if arg1[i] == "[":
                counter  += 1
            else:
                counter = counter - 1
        if counter > 0:
            print("Its not ok")
        else:
            print("Its ok")
        print(counter)    

br("[][][]][[]")

# Tenth task:
def charFreq(arg1):
    dictionary = {}
    for i in arg1:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1
    print(dictionary)
charFreq("abbabcbcbdbabababcbcbab") 

# Eleventh task:
def decToBin(arg1):
    result = ''
    i = arg1
    while i != 0:
        if i % 2 != 0:
            result = result + str('1')
        else:
            result = result + str('0')
        i = i // 2
    result = result[::-1]
    print (result)

decToBin(23)