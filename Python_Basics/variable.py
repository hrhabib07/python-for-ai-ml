#Store your name, age, and university in variables


name = "Habib"
age = 22
university = "Metropolitan University"
cgpa = 3.83



# Swap two numbers without using a third variable
first_number = 10
second_number = 20
first_number, second_number = second_number, first_number
print("After swapping:")
print("First number:", first_number)
print("Second number:", second_number)


a,b,c,d = 1,2,3,4
print(a,b,c,d)
a,b,c,d = d,c,b,a
print(a,b,c,d)

#Check type of: integer,float,string

print(f"""
Type of name: {type(name)}
Type of age: {type(age)}
Type of university: {type(university)}
Type of cgpa: {type(cgpa)}
""")