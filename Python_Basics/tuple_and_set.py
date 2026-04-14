
# tuple and set are two different data structures in Python.
# tuple is a collection of ordered and immutable elements. It is defined using parentheses ().
tp1 = (1,2,3,4,5,6) # tuple is immutable
print(*tp1) # it will print all the elements of the tuple without the parentheses and commas
tp1[2]=99 # it will give an error because tuple is immutable



#set is a collection of unique elements. It is unordered and unindexed. It is mutable but does not allow duplicate values.
st1 = {1,3,9,7, 9 ,  7 ,9} # set does not allow duplicate values
print(st1) # it will print only unique values
st2 = {2,3,5,7}
print(st1 & st2) # it will print the common values in both sets
print(st1 | st2) # it will print all the unique values in both sets
print(st1 - st2) # it will print the values which are in st1 but not in st2
print(st2 - st1) # it will print the values which are in st2 but not in st1 
