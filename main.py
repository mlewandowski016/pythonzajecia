#zadanie1
def apply_twice(func, data):
    return func(func(data))

result = apply_twice(lambda x: x + 2, 2)
print(result)

#zadanie2
def make_multiplier(x):
    def multipliter(n):
        return x * n

    return multipliter


double = make_multiplier(2)

print(double(5))

#zadanie3
data = [1,2,3,4,5,6,7,8,9,10]
def filter_even_numbers(data):
    evenNumbers = [x for x in data if x % 2 == 0]
    return evenNumbers

filteredNumbers = filter_even_numbers(data)
print("Liczby parzyste: ", filteredNumbers)

#zadanie4
import time
def timeit(func):
    def wrapper():
        startTime = time.time()
        func()
        endTime = time.time()
        totalTime = endTime - startTime
        print("Czas wykonania funkcji : ", totalTime)
    return wrapper
@timeit
def hello():
    print("Hello world!")

hello()

#zadanie5
data = [1, 2, 3, 4, 5]

square = list(map(lambda x: x * x, data))

print(square)

#zadanie6
data = [1, 2, 3, 4, 5]
def square(x):
    return x * x

squared = list(map(square, data))

print(squared)

#zadanie7
words = ["Krzesło", "But", "Butelka", "Banan"]

def filterLength(word):
    if len(word) > 5:
        return True
    else:
        return False

filteredWords = filter(filterLength, words)
for x in filteredWords:
    print(x)

#zadanie8
import functools

data = [1, 2, 3, 4, 5]

sum = functools.reduce(lambda a, b: a + b, data)
print(sum)

#zadanie9
squaredData = [2 ** i for i in range(10)]
print(squaredData)