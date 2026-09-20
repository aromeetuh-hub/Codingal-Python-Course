# input () always gives a STRING value
city = input("Enter your city: ")
temp = float(input("Enter the current temperature: "))

if temp > 35:
    print("WARNING: It is a very hot day today!")

if temp > 25:
    print("Great day to go outside")
else:
    print("Grab a jacket before you go out!")

if temp > 35:
    print("Weather: Schorching Hot")
elif temp > 25:
    print("Weather: Warm and Sunny")
elif temp > 15:
    print("Weather: Cool and Breezy")
else:
    print("Weather: Cold - stay warm!")    


if city == "Lagos":
    print("You live in Lagos")
elif city == "Dehli":
    print("You live in Dehli NCR")
elif city == "Dombivali":
    print("You live in Maharashtra")
elif city == "Abuja":
    print("You live in FCT")

# Adding ELSE is not necessary 

import datetime
now = datetime.datetime.now()
print(now)
