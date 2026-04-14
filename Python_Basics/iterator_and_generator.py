def f():
    print("Start")
    yield 1 # yield is used to return a value and pause the function execution until the next value is requested
    print("Middle")
    yield 2
    print("End")

k = f() # it will return a generator object which can be iterated to get the values yielded by the function
print(k) # it will print the generator object which is an iterator that can be used to iterate through the values yielded by the function
print(next(k)) # it will execute the function until the first yield statement and return the value yielded by the first yield statement which is 1
print(next(k)) # it will resume the function execution from where it was paused after the first yield statement and execute until the second yield statement and return the value yielded by the second yield statement which is 2
print(next(k)) # it will resume the function execution from where it was paused after the second yield statement and execute until the end of the function and since there are no more yield statements it will raise StopIteration exception


def f():
    yield 1
    yield 2

print(next(f())) # it will create a new generator object and execute the function until the first yield statement and return the value yielded by the first yield statement which is 1
print(next(f())) # it will create a new generator object and execute the function until the first yield statement and return the value yielded by the first yield statement which is 1 again because it is a new generator object and it starts from the beginning of the function