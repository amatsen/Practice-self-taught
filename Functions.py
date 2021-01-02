print("Welcome to Functions!, helper programs within the program")
def print_pi():  #part 1 define the function
    print(3.14159)
print_pi()    #part 2 call the function

def print_double(x):
    print(x * 2)
print_double(8)    

def get_pi():
    return 3.14159

##print(get_pi()) ## this is working so far

x = get_pi()
print(x)

def get_double(x):
    return x * 2
y = get_double(7)    
print(y)

def get_greatest(x, y):
    if x > y:
        return x
    else:
        return y   
greatest = get_greatest(10,42) 
print(greatest)        

def is_even(x):
    if x % 2 == 0: 
        return True
    else:
        return False

if is_even(40)== True: 
    print("It's Even!")
else:
    print("It's Odd!")    