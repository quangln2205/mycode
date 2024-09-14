# 1. Write a Python function to find the maximum of three number    
def my_func(x,y,z):
    if (x >= y) and (x >= z):
        return x
    elif (y >= x) and (y >= z): 
        return y
    else:
        return z

print(my_func(5,5,4)) # 6