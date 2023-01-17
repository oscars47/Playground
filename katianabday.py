# super secret message written in the lovely Python for Katiana
# enjoy ;)

import matplotlib.pyplot as plt # matplotlib oh yeah...
import numpy as np

# plotting criteria
plt.figure(figsize=(5,5))
plt.axis('off')
plt.axis('equal')
plt.xlim(-2, 7)
plt.ylim(-6, 2)

# define function to plot in form
# (x-x_offset)^2 + (y-y_offset)^2 = radius^2
# note: 'radius' is technically 'radius^2'
def circle_top(x, x_offset, y_offset, radius):
    # print(x, x-x_offset, radius - (x-x_offset)**2)
    if radius - (x-x_offset)**2 >= 0:
        y = np.sqrt(radius - (x-x_offset)**2) + y_offset
    else:
        y = y_offset
    return y

def circle_bottom(x, x_offset, y_offset, radius):
    if radius - (x-x_offset)**2 >= 0:
        y = -1*np.sqrt(radius - (x-x_offset)**2) + y_offset
    else:
        y = y_offset
    return y

def animate_circle(x_all_ls):
    for x_all in x_all_ls: # go through each list of info for each circle
        x = x_all[0]
        x_offset = x_all[1]
        y_offset = x_all[2]
        radius = x_all[3]
        
        # do animating
        x_current = []
        y_current_top = []
        y_current_bottom=[]
        for value in x:
            x_current.append(value)
            y_current_top.append(circle_top(value, x_offset, y_offset, radius))
            y_current_bottom.append(circle_bottom(value, x_offset, y_offset, radius))
            plt.plot(x_current, y_current_top, color='skyblue') # print top
            plt.plot(x_current, y_current_bottom, color='skyblue') # print bottom
            plt.pause(1e-9) # add delay to animate


# initialize x arrays
x1 = list(np.linspace(-1, 1, 1000))
x2 = list(np.linspace(.5, 4.5, 1000))
x3 = list(np.linspace(4, 6, 1000))

# package into lists
x1_all = [x1, 0, -.25, 1]
x2_all = [x2, 2.5, -2, 4.0]
x3_all = [x3, 5, -.25, 1]
x_all = [x1_all, x2_all, x3_all]

animate_circle(x_all)
plt.title('Happy Birthday, Katiana!', fontsize=22)
plt.show()
