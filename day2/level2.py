first_name = "Mathias"
last_name  = "N"
full_name  = "Mathias N"
country = "India"
city = "Marthandam"
age = 63
year = "1963"
income = 22.200

is_married = True
a,b,c,d,name,age=1,2,3,4,'Grace',24
print(name,age)

print(first_name,type(first_name),len(first_name))
print(last_name,type(last_name), len(last_name))
print(country,type(country))
print(age,type(age))
print(year,type(year))
print(is_married,type(is_married))
print(a,b,type(a),type(b))
print(income,type(income))
diff = len(first_name) ==len(last_name)
print (diff,type(diff))

total= a+b+c+d
mult= a*b*c*d
sub= a-b-c-d
div=a/b/c/d
f_div = a//b//c//d
mod = a//b//c//d
exp = a**b**c**d
print(total)
print(mult)
print(sub)
print(div)
print(f_div)
print(mod)
print(exp)

#calculating area & circumference of a circle
pi=3.14
radius=int(input("Enter radius :"))
area_of_circle = pi+radius**2
circum_of_circle = 2*pi*radius
print(circum_of_circle,"circ")
print(area_of_circle,"area")