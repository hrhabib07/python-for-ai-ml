def sqrIt(num) : 
    print(num*num)
sqrIt(4)

def add(a,b) : 
    return a+b
print(add(1,3))

def greet(name="User") : 
    print("Hello ", name)
    
greet()
greet("Habib")

def sumLi(li) :
    sum = 0
    for i in li : 
        sum+=i
    return sum
print(sumLi([1,2,3]))

def f(x):
    print(x * 2)

print(f(3))

# positional Arguement 
def greetWithName(name, age) : 
    print(name, age)
greetWithName("Habib",22)
greetWithName(age=22,name="Habib")

def power(base, exp=2) : 
    return pow(base,exp)
print(power(3))
print(power(3,3))

def mult(a:int, b:int) -> int :
    """This function multiplies two numbers"""
    return a*b
print(mult.__doc__)
print(mult(7,2))

def evenList(li) : 
    """This fucntion returns only even numbers from the list"""
    return [x for x in li if x%2==0]
print(evenList([1,2,3,4,5]))


