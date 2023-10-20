#1
import numpy as np 
def sine(x):        #define a function of sine(x) to return sin(x)
    return np.sin(x)

#2


def cosine(x):      #define a function of cosine(x) to return sin(x)
    return np.cos(x)

#3

x_val=np.linspace(0,2*np.pi,1000) # creating an array of x values between 0 and 2pi with 1000 entries 
sin_val=[sine(x) for x in x_val] # calculate sin() for the values of x 
cos_val=[cosine(x) for x in x_val] # calculate cos() for the values of x 

#4

print("x     sin(x)     cos(x)")  #prints x, sin(x) and cos(x) in one line
print("-" *24)  #and the header line
for i in range (10): # Iterate through the first 10 values of x,sin x and cosx
    x=x_val[i]
    sinx=sin_val[i]
    cosx=cos_val[i]
    print(f"{x:.2f} {sinx:.6f} {cosx:.6f}") # prints the values in columen
