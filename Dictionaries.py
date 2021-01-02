print("Dictionaries, ya'll!") # lists are ordered but dictionaries are not
# remmember those braces, ya'll
Grades= {"Ralphy": 98, "Benjamin":42, "Alice":87, "Angie":78, "Argunaught": 88}
print(Grades)
print(len(Grades))
Grade = Grades ["Alice"]
print(Grade)

Grades["Bobby"] = 57
print(Grades)

for name in Grades:
    grade = Grades[name]
    print("The grade for {} is {}".format(name, grade))