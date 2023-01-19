# file to make animated gifs of the single and double pendulum phase spaces

using Plots
# Plots.default(show = true)
using DifferentialEquations

# first define the diffeq system
# write a function which updates a vector that is designated to hold the solution
function pendulum_param!(du, u, p, t) # du, u are the derivative and standard function vector; p is a vector holding the parameters, t is the times
    θ, v = u
    L, g = p
    k = g / L

    du[1] = dθ = v
    du[2] = dv = -k*sin(θ)
end

# define initial conditionals
u0 = [pi/2; 0.0]
tspan = (0.0, 10.0)
p = [1.0, 9.8]

# now solve
prob = ODEProblem(pendulum_param!,u0,tspan,p)
sol = solve(prob)
println("here")
plot(sol)

# x = range(0, 10, 100)
# y = sin.(x)
# plot(x, y)
readline()