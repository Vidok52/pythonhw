
#First task:
def printer(str1):
    print("Hello {0}!".format(str1))

# printer("Anton")

#Second task
def sum(list1):
    result = 0
    for i in list1:
        result = result + i
    return result

def multiply(list1):
    result = 1
    for i in list1:
        result = result * i
    return result

# rand = [1,2,3,4,5,6]

# sum(rand)
# multiply(rand)

#Third task:

def reverse(str1):
    result = str1[::-1]
    return result

print(reverse("Anton"))

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
        return("True")
    else:
        return("False")
    
#Fifth task:

def histogram(lst1):
    result = []
    for i in lst1:
        result.append(i * "=##=")
    return result
print(histogram([4,2,3]))

# Sixth task:

def caesarCipher(str1, key=2):
    print ("As was: ",str1)
    ChipStr1 = ""
    for i in str1:
        num1 = ord(i)
        chr1 = chr(num1 + key)
        ChipStr1 = ChipStr1 + chr1
    print ("As is: ", ChipStr1)
    return ChipStr1
  
# Seventh task:

import random
import copy

def  diagonalReverse(matrix):
    # matrix = [[random.randrange(0,10) for i in range(row)] for z in range(col)]
    # matrix = [[1,2,3],[2,3,1],[3,1,2]]
    print("As was:")
    for z in range(len(matrix)):
        print(matrix[z])
    print("As is:")
    NewMatrix = copy.deepcopy(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            NewMatrix[i][j] = matrix[j][i]

    for i in NewMatrix:
        print(i)
    return NewMatrix

# Eights task:
 
def game(arg1, arg2):
    a = random.randint(arg1,arg2)
    b = int(input("Please input you digit:"))
    while a !=  b:
        print(a)
        print("Try again")
        b = int(input("Please input you digit:"))
    return("You got it!")

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
        return("Its not ok")
    else:
        return("Its ok")   

# Tenth task:
def charFreq(arg1):
    dictionary = {}
    for i in arg1:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1
    return(dictionary)

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
    return result

