print("Want to learn about lists?")
names = ["Brian", "AnnMarie", "David", "Joey", "Jacob", "Danny"]
print (names)
print("The length of the list is: ", len(names))
print("Lets add mom and dad")
names.append("Sarah")
names.append("Butch")
print(names)

for index in range(0, len(names)):
    print(names[index])

print(" ")
print("Now just the kids")    

for index in range(0, len(names)-2):
    print(names[index])

#for name in names:
#    print(names)    

print(" ")
print("time to sort everybody")
names.sort()
for names in names:
    print(names)  