z= "Conditional's Practice"
z = z .upper()
print(z)

print ("Is 8 greater than 3?") # != is not equal
if 8 > 3:
    print(True)

x = 7
y = 5
print(" Is {} greater than {}?".format(x,y)) 
if x > y:
    print(True)
else:
    print(False)     

x = 2
y = 5
print(" Is {} greater than {}?".format(x,y)) 
if x > y:
    print(True)
else:
    print(False)     

print("Do you want to play a game?")
mario = "down"
luigi = "up"  

if mario == "up" or luigi == "up":
    print("someone moves up")
if mario == "up" and luigi == "down":
    print("Mario gets 1-up")
elif mario == "down" and luigi == "up":
    print("Luigi gets 1-up")
elif mario == "down" and luigi == "down":
    print("both parties fall down")            

