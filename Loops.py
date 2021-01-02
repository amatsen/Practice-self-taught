print("Loops Practice")
print("Lets get at them loops!")

for x in range(0, 11, 2):      # count by 2's  # count down by ones if -1, is not working
    print(x)
title = "The Black Parade"
for index in range(len(title)-1, -1, -1): # don't forget to switch start and end for backwards
    print(title[index])

for letter in title:
    print(letter)

# while (True):
#    print("The End")    
