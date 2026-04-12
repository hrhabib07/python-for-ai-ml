integer_number = 10
float_number = 3.19
string_name = "Gamlish"
is_published = False
print(f"""
type of Int : {type(integer_number)}
type of Float : {type(float_number)}
type of String : {type(string_name)}
type of Boolean : {type(is_published)}
""")

# conversion from one type to anther type 
str_25 = "25"
print(type(str_25))
str_25 = int(str_25)
print(type(str_25))
str_3f5 = "3.5"
print(type(str_3f5))
str_3f5 = float(str_3f5)
print(type(str_3f5))


