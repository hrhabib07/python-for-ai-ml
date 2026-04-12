for i in range(4): # print from 0 to 3; 4 exclusive
    print(i)
print("\nSecond loop starts here")
for i in range(10,15): # it will print from 10 to 14; 15 exclusive
    print(i)
print("\nThird loop starts here")
for i in range(10,19,5): #it prints 10 to 18 with 5 skipped in each steps
    print(i)
#Print numbers from 1 to 10 using for loop
print("\nPrinintg 1 to 10 starts here")
for i in range(1,11) : 
    print(i)
#Print even numbers from 1 to 20
print("\nPrinting even 1 to 20 starts here")
for i in range(2,21,2) : 
    print(i)
    
# printing reverse using while loop from 5 to 1
print("\nprinting reverse using while loop from 5 to 1 starts here")
k = 5
while k>0 : 
    print(k)
    k-=1
    
# loop + if else 
print("\nLoop + if else starts here")
for i in range(1,11) : 
    if i % 3 == 0:
        print("Fizz")
    else:
        print(i)
