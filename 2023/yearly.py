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
op_dict = {'1': '+', '2': '-', '3': '*', '4': '/', '5': '**', '-2': '(', '-3': ')'}

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

#print(p_perm[0])

# custom function to calculate operation perms
def get_op_perms(p_ls, input=0): # takes in current p list and input numbers
    op_temp_all_f = [] # list to hold formatted op_temps

    def temp_format(op_temp): # nested function to format the op_temps from [(2), (1, 2, 3, 4, 5), (0)] => [(2, 1, 0), (2, 2, 0), etc]
        temp_all = []
        # get count of full operations lists; this determines the r value for permutations
        r = op_temp.count(operations)
        if r > 0:
            # add restrictive permutations as well
            choice_perm = []
            for i in range(len(operations)):
                restricted_op = operations[:len(operations)-i]
                # print(restricted_op)
                # duplicate each element 4 times
                raw_perm = []
                for num in restricted_op:
                    for m in range(4):
                        raw_perm.append(num)
                #print(raw_perm)
                # now get permutations
                processed_perm = list(permutations(raw_perm, r))
                # get unique processed perms
                processed_perm = list(set(processed_perm))
                #print(processed_perm)
                choice_perm.append(processed_perm)
            
            #combine them all
            choice_perm_all = []
            for choice_ls in choice_perm:
                for choice in choice_ls:
                    choice_perm_all.append(choice)
            # get unique
            choice_perm_all = list(set(choice_perm_all))
            # print(choice_perm_all)



            # print('op_temp', op_temp)
            #print('choice perm', choice_perm)
            
            # iterate through all of the op_temps; if full operations, assign each of the r-permutations
            for choice in choice_perm_all: # do this r times
                temp = []
                c = 0 # counter to tell how many of the r we've done, so what integer to choose in perm tuple
                for op_tuple in op_temp:
                    if len(op_tuple) ==1: # if just a single number
                        temp.append(op_tuple[0])
                    else:
                        temp.append(choice[c])
                        c+=1
                temp_all.append(temp) # append to main list
        print('temp all', temp_all)
        return temp_all


    # def is_leading_0(op_temp): # call function to check if leading 0s; if true, then call int_split

    # def split_int()

    # def compute_val()
    # want only unique
    p_ls = list(set(p_ls))
    #print(p_ls)
    for p_tuple in p_ls:
        op_temp = []
        for k, p in enumerate(p_tuple):
            if (p==0):
                op_temp.append([0])
            elif (k == 0) and (p==-1):
                op_temp.append([2])
            else:
                op_temp.append([i for i in operations])
        #print(op_temp)
        op_temp_all_f.append(temp_format(op_temp)) # append the formatted list of op lists
        #print(temp_format(op_temp))
        

# call get_op_perms for all inputs and all perms-----------------
# for inp in input_perm:
for i, p in enumerate(p_perm):
    get_op_perms(p)

# print(operations_perm[-1])




tf = time.time()
print('Compute time = %.3fs' % (tf-t0))
