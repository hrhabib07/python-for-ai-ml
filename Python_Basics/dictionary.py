student = {
    "name":"Habib",
    "age": 22,
    "university":"MU"
}

for value in student.values(): 
    print(value)
    
student["age"] = 23
student["cgpa"] = 3.83

for key, value in student.items() : 
    print(key, value)

if "email" in student : 
    print("eamil found")   
print(student.get("email", "Not Found"))

students = {
    "s1": {"name": "A", "marks": 80},
    "s2": {"name": "B", "marks": 70}
}

print(students["s1"]["name"])
print(students["s2"]["marks"])

print(student)