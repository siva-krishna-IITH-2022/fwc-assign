import numpy as np
from matplotlib import pyplot as plt
#if using termux
import subprocess
import shlex
from scipy.integrate import quad
#Defining f(x)
def f(x,a,b,c,d):
        return a * x**3 + b * x**2 + c*x + d 
a = 1
b = 1
c = -1
d = 2
label_str = "$x^3 + x^2 - x + 2$"

#For minima using gradient ascent
cur_x = 0.1
alpha = 0.001 
precision = 0.00000001 
previous_step_size = 1
max_iters = 100000000 
iters = 0

#Defining derivative of f(x)
df = lambda x: 3*a*x**2 + 2*b*x + c  
#----------------    Maximum    ----------------------          
#Gradient ascent calculation
while (previous_step_size > precision) & (iters < max_iters) :
    prev_x = cur_x             
    cur_x += alpha * df(prev_x)   
    previous_step_size = abs(cur_x - prev_x)   
    iters+=1  
min_val = f(cur_x,a,b,c,d)
print("Maximum value of f(x) is ", min_val, "at","x =",cur_x)
#-----------------   Minimum    -----------------------
cur1_x = 0.1
alpha = 0.001 
precision = 0.00000001 
previous_step_size = 1
max_iters = 100000000 
iters = 0

while (previous_step_size > precision) & (iters < max_iters) :
    prev_x = cur1_x             
    cur1_x -= alpha * df(prev_x)
    previous_step_size = abs(cur1_x - prev_x)   
    iters+=1  

max_val = f(cur1_x,a,b,c,d)
print("Minimum value of f(x) is ", max_val, "at","x =",cur1_x)
#------------------    Integration    ------------------

x=np.arange(0,3.1,0.1)
def integrand1(x):
    return (x**3+x**2-x+2)
A1,err=quad(integrand1, -1, 1)
print("Integration from -1 to 1 is : ",A1)
#Plotting f(x)
x=np.linspace(-5,5,1000)
y=f(x,a,b,c,d)
plt.plot(x,y,label=label_str)
#Labelling points
plt.plot(cur_x,min_val,'o')
plt.plot(cur1_x,max_val,'o')
plt.text(cur_x, min_val,f'P({cur_x:.2f},{min_val:.1f})')
plt.text(cur1_x, max_val,f'Q({cur1_x:.2f},{max_val:.1f})')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid()
plt.legend()
#plt.show()
plt.savefig('/sdcard/DCIM/Assignment-7/codes/opt.pdf')
subprocess.run(shlex.split("termux-open sdcard/DCIM/Assignment-7/codes/opt.pdf"))
