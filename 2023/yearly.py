###
# file to solve MIT's "yearly" challenge.
# @ oscars47
# problem description: how many integers from 1 to 100 can you form using the digits of the year (e.g., 2023)
#                       exactly once each along eith the operators + - * / and ^ (exponentiate).
#                       note that parantheses don't count as operations.
#                       preference for fewer operations; with the same number of operations prefer the order of the year.
###

import time # to log how long comoputations take
from itertools import permutations # to get permutations

# define list of operations
# 1 is +
# 2 is -
# 3 is *
# 4 is /
# 5 is ^ (**)
# we reserve 0 for no operation
operations = list(range(1, 6, 1))

# input = str(input('Enter a 4-digit year (e.g., 2023)'))
input='2023'
# convert to list of integers
input_ls = [int(c) for c in input]

t0 = time.time() # start the clock

input_perm = list(permutations(input_ls)) # get permutations of input number

# initialize lists holding operations which we will permute
# 0 indicates no operation, -1 indicates an operation yet to be determined
p0 = [0 for i in range(len(input))]
p0[0]=-1
p1 = [0 for i in range(len(input))]
p1[0]=p1[1]=-1
p2 = [0 for i in range(len(input))]
p2[0]=p2[1]=p2[2]=-1
p3 = [-1 for i in range(len(input))]
p3[-1]=0
p4 = [-1 for i in range(len(input))]
# add them all to list; don't include p4 though since we don't want permutations on a vector of all the same entries
p_3 = [p0, p1, p2, p3]

# perform position permuations
p_perm = [list(permutations(p)) for p in p_3]
p_perm.append([tuple(p4)])
# print(p_perm)
# print(len(p_perm))
# print(len(p_perm[1]))

# now figure out possible operations, the integers to be used in the calcultations, and the final answer
# for the first two, we use list of list of tuples; for the value, just list of lists of integer
operations_perm = []
int_order = []
int_value = []

print(p_perm[0][0][0])

# custom function to calculate operation perms
# def get_op_perms(p_ls, r): # takes in current p list and r parameter (size of groups)
#     for p_tuples in p_ls: # get all tuples in p
#         for p_tuple in p_tuples: # iterate through each p_tuple
#             for j, p in p_tuple: # iterate through each element in p_tuple
#             # if 1st index of p_tuple is 


# for i, p in enumerate(p_perm):
#     operations_temp= list(permutations(operations, i+1)) # list to hold the operations tuples. permute in groups of size = number of operations
#     operations_perm.append(operations_temp)

# print(operations_perm[-1])




tf = time.time()
print('Compute time = %.3fs' % (tf-t0))
