import math

print("This program calculates the volume of")
print("a cylinder given radius and height")


#Input
r = int(input("What is the radius: "))
h = int(input("What is the height: "))

#Process
v = math.pi*r*r*h
v = round(v,3)

#Output
print("The volume of a cylinder with")
print("r = ",r," units")
print("h = ",h," units")
print("is ",v," units cubed")
