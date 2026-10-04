# _ _ _ _ School Class Organizer _ _ _ _
classmates = ["Aarav", "Priya", "Rahul", "Sneha", "Dev"]
print("Class list: ", classmates)

print("Total students: ", len(classmates))
print("First student: ", classmates[0])
print("Last Student: ", classmates[-1])
print("First three: ", classmates[:3])

classmates.append("Meera")
print("\nAfter adding Meera: ", classmates)
classmates.remove("Dev")
print("After removing Dev: ", classmates)
classmates.sort()
print("Sorted alphabetically: ", classmates)
classmates.reverse()
print("Reversed: ", classmates)

teacher = {"name ": "Mr Sharma", "Subject": }