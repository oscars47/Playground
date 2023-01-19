import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as sci

# enable latex
plt.rcParams["mathtext.fontset"]

# returns [dtheta, dv]
def pendulum(s, t, L=1, g=9.8):
    k = g / L
    # print(s)
    return np.array([
        s[1],
        -k*np.sin(s[0])
    ])

# time steps
max_T = 10
dt = 0.01
# time range
time = np.arange(0.0, max_T, dt)

# initial conditions
s0 = [np.pi/2, 0]
L = 1
g = 9.8

# store results
# state_history = []

# initialize sk
# sk = s0
# initialize time
# t = 0

sol = sci.odeint(pendulum, s0, time, args=(L, g))

# for t in time:
#     state_history.append(sk)

#     sk = sci.RK45(fun=pendulum, t0=t, y0=sk, t_bound = max_T, first_step=dt)

# # convert state history to np array
# state_history = np.array(state_history)
# print(state_history)

# begin plotting
fig = plt.figure()  # figsize=(10, 8)
ax = plt.axes(projection='3d')
ax.plot3D(sol[:, 0], sol[:, 1], time)
plt.show()


# ax.set_xlim3d(min(state_history[:, 0]) - 0.05, max(state_history[:, 0]) + 0.05)
# ax.set_ylim3d(min(state_history[:, 1]) - 0.05, max(state_history[:, 1]) + 0.05)
# ax.set_zlim3d(min(time)-0.05, max(time)+0.05)

# # set figure elements
# ax.set(xlabel='$\omega$', ylabel='$v$', zlabel='$t$')
# ax.set_title("Pendulum for L = "+f'{L:.3g}'+"m, g = "+f'{g:.3g}'+"$m/s^2$ at t= "+f'{max(time):.3g}'+"s")

# ax.plot3D(state_history[:, 0], state_history[:, 1], time)
# plt.show()

# # define trajectory vector
# trajectory, = ax.plot([], [])

# # function to do animation
# def animate(i):
#     ax.set_title("Pendulum for L = "+f'{L:.3g}'+"m, g = "+f'{g:.3g}'+"$m/s^2 at t= "+f'{')