name = input("Enter patient name: ")
age = int(input("Enter patient age: "))

if age > 40:
    print(name, "should take HIGH dosage medicine")
else:
    print(name, "should take LOW dosage medicine")
