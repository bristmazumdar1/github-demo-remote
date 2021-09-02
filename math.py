#add implementation
def add(x,y):
    return x+y
#substract implementation
def subtract(x,y):
    return x-y             #on master branch
#multiply implementation
def multiply(x,y):
    return x*y			#on bug456 branch
#divide implementation
def divide(x,y):
    if y==0:                     #on master branch
	return DIVIDE_BY_0_ERROR 
    else:
	return x/y
#square implementation
def square(x):
    return (x*x)



