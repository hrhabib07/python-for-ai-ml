num = int(input("I will tell you positive, negavive or Zero. Enter your number : "))
if(num > 0) : 
    print("Positive")
elif (num<0) :
    print("Negative")
else : 
    print("Zero")
    



marks = int(input("Enter your marks. I will tell you grade. Your marks: "))
if 0<= marks <=100 : 
    if marks >= 80 : 
        print("A+")
    elif marks >= 70 : 
        print("A")
    elif marks >=60 : 
        print("B")
    else : print("fail")
else : 
    print("Invalid Marks!!!")


  
    
    
age = 25
has_id = True

if age >= 18 and has_id : 
    print("Allowed")
else : print("Not Allowed")