def area_of_circle(radius):
    area=3.14*radius*radius
    return area
r=float(input("Enter the radius of the circle:"))
area=area_of_circle(r)
print("Radius of circle:",r)
print("Area of circle:",area)
