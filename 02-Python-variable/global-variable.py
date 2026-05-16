x = 'sakib' #This is a global variable cause it outside of a function.
def my_function():
    x ='rajib'# This is a local variable cause it inside of my_function code block.  
    print("This is " + x)
my_function()
print("This is " + x)

A = 23 
def secondFunction():
    global A # use global keywork to make varable global even when it is in function. 
    A = 40 # global keyword even changed the value of varaiable by updating latest one .
secondFunction()
print(A)