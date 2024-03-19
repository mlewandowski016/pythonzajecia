from itertools import product

#zadanie 1
list1 = ['A', 'B']
list2 = ['C', 'D']
print(list(product(list1, list2)))

#zadanie 2
def varianter(list1):
    print(list(product(list1,list1)))

varianter(list1)

#zadanie 3
def fibonacci():
    a = 0
    b = 1
    for i in range(10):
        print(b)
        a, b = b, a + b

fibonacci()

#zadanie 4
dataA = [1,2,3,4,5,6,7,8,9,10]

dataB = [pow(x,2) for x in dataA if (sum := pow(x,2) > 10)]

print(dataB)

#zadanie 5
word = "Kajak"

def isPalindrome(word) : print('this word is palindrome') if word.lower() == word[::-1].lower() else print ('this word is not palindrome')

isPalindrome(word)

#zadanie 6
def safe_function(func):
    def errorHandler():
        try: func()
        except: print("Error!")
    return errorHandler()

a = 4
b = 2

@safe_function
def func(a, b):
    sum = a / b
    return sum

data = func(4, 2)
print(data)