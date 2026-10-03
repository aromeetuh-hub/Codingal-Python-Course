def rectangle(length, breadth):
    return length * breadth

def circle(radius):
    return 3.14 * radius * radius

def triangle(base, height):
    return 0.5 * base * height

print("Area of a rectangle: ")
l = int(input("Enter length of rectangle: "))
b = int(input("Enter breadth of rectangle: "))
print("Area(rectangle) = ", rectangle(b, l))

print("Area of a circle: ")
r = int(input("Enter radius of circle: "))
print("Area(circle) = ", circle(r))

print("Area of a triangle: ")
b = int(input("Enter base of triangle: "))
h = int(input("Enter height of triangle: "))
print("Area(triangle) = ", triangle(b, h))