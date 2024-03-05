from functools import reduce

#zadanie1
print('zadanie 1')

print(hex(2024))

x = -32
print(abs(x))

data = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
print(max(data))

print(pow(x, 2))

print(ord('a'))

#zadanie2
print('zadanie 2')
from zadanie2 import *
welcome()

#zadanie3
print('zadanie 3')
def fun1():
    x = 12
    print("wartość x wewnątrz funkcji: ",x)

fun1()
print("wartość x poza funkcją: ",x)

#zadanie4
print('zadanie4')
def funz4_a():
    return 10
def funz4_b(funz4_a):
    print("Funkcja funz4_a zwaraca za pomocą return wartość: ", funz4_a())
funz4_b(funz4_a)

#zadanie5
print('zadanie5')
numbers = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
def isEven(list):
    for i in list:
        if (i % 2 == 0):
            print(i)
isEven(numbers)

x = lambda a, b : a * b
print('Pole kwadratu:', x(5, 6))

#zadanie6
print('zadanie 6')
def start_a(name):
    return list(filter(lambda x: x[0] == 'A', name))
def pow_list(data):
    return list(map(lambda x: x*x, data))

print(start_a(['Adam', 'Mateusz', 'Adrian']))
print(pow_list([1, 2, 3, 4, 5]))

#zadanie7
print('zadanie 7')
square = lambda number: number * number
plusFive = lambda number: number + 5
addNumbers = lambda a,b: a + b

def apply(data):
    data = map(square, data)
    data = map(plusFive, data)
    return list(data)

def applyToList(functions, args):
    for f, n in zip(functions, args):
        print(f(*n) if isinstance(n, tuple) else f(n))

applyToList([square, plusFive, addNumbers], [5, 10, (10, 15)])


#zadanie8
print('zadanie 8')
squaresList = [x**2 for x in range(1, 11)]

wordsList = ["gruszka", "banan", "jabłko", "kiwi"]
wordLengths = [len(word) for word in wordsList]

print("Liczby kwadratowe", squaresList)
print("Długość słów:", wordLengths)

#zadanie9
print('zadanie 9')
data = [1, 8, 3, 4, 5]
def max(data):
    return reduce(lambda x, y: x if x > y else y, data)

def average(data):
    sum = reduce(lambda x, y: x + y, data)
    return sum / len(data)

print("największa liczba:", max(data))
print("srednia", average(data))

#zadanie10
print("zadanie 10")
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def fileReader(path):
    with open(path) as file:
        for line in file:
            print(line)

data = fibonacci()
for i in range(100):
    print(next(data))

#fileReader("sampletext.txt")