#n.b. use julia name.jl to compile

# import some packages
using Printf
using Statistics

# define variables
s = 0
s = "Dog"
println(s)

# function
 function changeNum()
    # assert datatype
    x::Int8 = 10
    x = "Dog"
 end

 # gives error
#  changeNum()

 # booleans; need to use all lowercase
 canDrive = true

 # other datatypes: BigFloat, BigInt

 # characters: single quotes
 c = 'h'

 # can cast datatypes
 c2 = Char(120)
 println(c2)

 # uint is unsigned integer, so strictly positive
 i1 = UInt8(trunc(3.14))
 println(i1)

 f1 = parse(Float64, "1")
 println(f1)

 i2 = parse(Int8, "1")

 # strings-----------
 s1= "hello world\n"
 println(length(s1))
 # starts index with 1!!
 println(s1[1])
 println(s1[end])
 println(s1[1:4])
 s2 = string("hello", " world")
 println(s2)
 println("hello"*" world")
 i3 = 2
 i4 = 3
 println("$i3 + $i4 = $(i3+i4)")

 # multiline strings
 s3 = """ I
 have
 many
 lines"""

 # string comparisons
 println("hello" > "world")

# get index
println(findfirst(isequal('i'), "Keigo"))
println(occursin("key", "monkey"))

# conditionals------
# &&: and. ||: or. !: not
age = 12
if age >= 5 && age <= 6
    prinln("kindergarten")
elseif age >= 7 && age <= 13
    println("middle")
elseif age >= 14 && and age <= 18
    println("high school")
else
    println("home")
end

# string formatting uses '@'
# latter part is called ternary operator
@printf("true || false = %s\n", true || false ? "true" : "false")
@printf("!true = %s\n", !true ? "true" : "false")

# loops---------
i = 1
while i < 20
    if ( i %2) == 0
        println(i)
        global i += 1
        # continue skips the immediate next value
        continue
    println(i)
    end
    global i+=1
    if i >= 10
        break
    end
end

i = 1
for i = 1:5
    println(i)
end

for i in [2, 4, 6]
    println(i)
end

# for j: from 2 to 10 with step size pf 2
for i = 1:5, j = 2:2:10
    println((i, j))
end

# arrays--------
# 2x2 with int32
a1 = zeros(Int32, 2, 2)

# undeinfed values
a2 = Array{Int32}(undef, 5)

a3= Float64[]

a4=[1,2,3]

println(a4[1])
println(a4[end])
println(5 in a4)
println(findfirst(isequal(2), a4))
# generic function
f(a) = (a >= 2) ? true : false
println(findall(f, a4))
println(count(f, a4))

# get sizes
println(size(a4))
println(length(a4))
println(sum(a4))

# put values at certain index
#splice!(a4, 2, [8, 9])
splice!(a4, 2:1, [8, 9, 10]) # this differs from the above bc we specify how many elements we replace
println(a4)
# remove items
splice!(a4, 2:3)
println(a4)
println(maximum(a4))
println(minimum(a4))

# can perform calcualtions on array like np array
println(a4 * 2)
println(a4)

# can store multiple datatypes inside array
a5=[1, 3.14, "hello"]
# println(a5*2) # throws error

# can store functions inside array!
a6 = [sin, cos, tan]
for n in a6
    println(n(0))
end

a7 = [1 2 3; 4 5 6]
println(a7)
for n = 1:2, m = 1:3
    @printf("%d ", a7[n, m])
end
println()

# every row in second column
println(a7[:, 2])
# every column in second row
println(a7[2, :])
# ranges
a8 = collect(1:5)

a9 = collect(2:2:10)
# can do backwards step

for n in a9 println(n) end

a10 = [n^2 for n in 1:5]
println(a10)

# add values to array
push!(a10, 36)
println(a10)

a11 = [n*m for n in 1:5, m in 1:5]
print(a11)

# 5 random 5 digit numbers 
a12 = rand(0:9, 5, 5)
for n = 1:5
    for m = 1:5
        print(a12[n, m])
    end
    println()
end

# tuples-----------
# tuple values are immutable
t1 = (1, 2, 3, 4)
println(t1)
println(t1[1])
for i in t1
    println(i)
end
# mutlidimensional tuples
t2 = ((1,2), (3,4))
println(t2[1][1])

t3 = (sue = ("Sue", 100), paul = ("Paul", 23))
println(t3.sue)

# dictionaries-------
# key must be unique
d1 = Dict("pi"=>3.14, "e" => 2.718)
println(d1["pi"])
d1["golden"] = 1.618 # can add key-value pairs
# delete value
delete!(d1, "pi")
println(d1)
println(haskey(d1, "pi"))
println(in("pi" => 3.14, d1))

println(keys(d1))
println(values(d1))

for kv in d1
    println(kv)
end

for (key, value) in d1
    println(key, " : ", value)
end

# set-----------
# only contains unique
st1 = Set(["Jim", "Pam", "Jim"])
println(st1)

# can add elements
push!(st1, "Michael")
# check for individual values using in
println(in("Dwight", st1))
# combine sets
st2 = Set(["Stan", "Mer"])
println(union(st1, st2))

# intersection
println(intersect(st1, st2))
println(setdiff(st1, st2))



# functions!! ---------------
getSum(x,y) = x+y
x,y=1,2
# for string formatting codes see my discord julia-misc
@printf("%d + %d = %d\n", x, y, getSum(x, y))