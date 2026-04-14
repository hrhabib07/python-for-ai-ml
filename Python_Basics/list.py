li = [1,2,3,4,5]
print(li[0]) #printing the first element of a list
print(li[-1]) #printing the last element of a list
print(len(li)) #prints the lenght of the list

nli = [10, 20, 30, 40, 50]
#first 3 elements
print(nli[:3])
#last 2 elements
print(nli[-2:])
#elements at even index
print(nli[::2])


uli = [1, 2, 3, 4]
print(*uli)
uli[1]=20;
print(*uli)
uli.append(5)
print(*uli)
uli.remove(3)
print(*uli)


li3 = [12, 5, 18, 25, 7]
for i in li3 : 
    if i > 10 : 
        print(i)
        
        
a = [1, 2, 3]
b = a
print(a)
print(b)
b[1] = -9
print(a)
print(b)

#why both changes? because b is not a copy of a it bascialy pointing the lcoation of a in memory.


#→ Create new list with squares using list comprehension
li = [1, 2, 3, 4, 5]
sqLi = [x**2 for x in li ]
print(sqLi)

#Create list of numbers divisible by 10
li = [10, 15, 20, 25, 30]
li3 = [x for x in li if x%10==0]
print(li3)

li = [12, 5, 18, 25, 7] 
li2 = [x*3 for x in li if x > 10]
print(li2)

# What will this output? [x for x in range(5) if x % 2 == 0]
#Ans: [0, 2, 4]