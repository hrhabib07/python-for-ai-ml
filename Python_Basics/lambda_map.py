cube = lambda a : a*a*a # lambda function is an anonymous function which can take any number of arguments but can only have one expression. It is defined using the lambda keyword followed by the arguments and a colon and then the expression. The expression is evaluated and returned when the function is called.
print(cube(2))
li = [2,3,4,5]

result = list(map(lambda x : x* x, li)) # map function is used to apply a function to all the items in an iterable (like list, tuple etc.) and return a map object which is an iterator that can be used to iterate through the values returned by the function for each element in the iterable. The first argument of the map function is the function to be applied and the second argument is the iterable. In this case we are using a lambda function to square each element in the list li. The map function will apply the lambda function to each element in the list li and return a map object which can be converted to a list using the list function. The resulting list will contain the squares of the elements in the original list li.
print(result)

li1 = [1,2,3]
li2 = [10,20,30]

result = list(map(lambda a,b : a+b, li1, li2)) # in this case we are using a lambda function to add the corresponding elements of the two lists li1 and li2. The map function will apply the lambda function to the first elements of both lists, then to the second elements of both lists and so on until it reaches the end of the shorter list. The resulting list will contain the sums of the corresponding elements of the two lists li1 and li2.
print(result)

li =[5,10,15]
result = list(map(lambda x : x *2, li))
print(result)

m = map(lambda x: x+1, [1,2,3])
print(m) # it will print the map object which is an iterator that can be used to iterate through the values returned by the lambda function for each element in the list
print(list(m)) # it will convert the map object to a list and print the list of values returned by the lambda function for each element in the list