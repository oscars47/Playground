###
# file to solve MIT's "yearly" challenge.
# @ oscars47
# problem description: how many integers from 1 to 100 can you form using the digits of the year (e.g., 2023)
#                       exactly once each along eith the operators + - * / and ^ (exponentiate).
#                       note that parantheses don't count as operations.
#                       preference for fewer operations; with the same number of operations prefer the order of the year.
###

import time # to log how long computations take
from itertools import permutations # to get permutations
from sympy import solve # for solving string equations
from sympy.abc import x
from sympy.parsing.sympy_parser import parse_expr

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
op_perm_all = []
int_order_all = []
int_val_all = []

#print(p_perm[0])

# function to build  equation in strings
def build_eq(int_split_temp, op_temp):
    eqn = ""
    for t, op in enumerate(op_temp):
        if op==0:
            eqn.append(int_split_temp[t])
        else:
            eqn.append(op_dict[str(op)])
    
    return eqn # note to actually solve this need to add 'x=' to beginning and call the compute function


# custom function to calculate operation perms
def update(p_ls, inp): # takes in current p list and input numbers
    # op_total = [] # finalized list of all formatted op_temps
    # int_order_temp = [] # list to hold integers broken up by operations
    # int_val_temp = [] # list to hold computations for the integers and the operations

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
        #print('temp all', temp_all)
        return temp_all

    # helper function to compute string representation of split integers
    def parse_split_str(op_temp, inp):
        int_split_str = [] # list to hold split integers as strings
        for d, op in op_temp:
            temp_split = ''
            if (op==0) or ((op != 0) and (d == 0)): # continue appending to the temp so long as this holds
                temp_split+=inp[d]
            else: # append temp_split to int_split_str and move on
                temp_split+=inp[d]
                int_split_str.append(temp_split)
        return int_split_str

    def is_not_leading_0(op_temp, inp): # call function to check if no leading 0s; if true, then call int_split
        int_split_str = parse_split_str(op_temp, inp)
        for int_split in int_split_str:
            if (int_split[0]=='0') and (len(int_split[0]) > 1): # if first index is 0 of multicharacter integer, then return false: i.e. there IS a leading 0
                return False
        return True # if we haven't returned False, it must be True
        

    def check_paren(op_temp, inp): # function to return a list of parenthesis variations

        

    def split_int(op_temp, inp): # asssumes not leading 0
        int_split_str = parse_split_str(op_temp, inp)
        int_split_int = [] # new list to hold the integer versions
        for int_split in int_split_str:
            int_split_int.append(int(int_split))
        return int_split_int

    def compute_int_val(int_split_temp, op_temp):
        eqn = build_eq(int_split_temp, op_temp)
        eqn = "x="+eqn
        # the code below in this function is adapted from https://stackoverflow.com/questions/30775453/converting-a-string-into-equation-and-resolve-it
        try:
            lhs =  parse_expr(eqn.split("=")[0])
            rhs =  parse_expr(eqn.split("=")[1])
            value = solve(lhs-rhs)
            return value
        except:
            print("invalid equation:", eqn)
            return -1 # return a value that will get filtered out by compute_pass
    
    def compute_pass(int_val):
        return ((int(int_val) - int_val == 0) and (int_val >= 1) and (int_val <= 100)) # conditions stated in problem

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
        # get formatted op_temp
        op_temp_f = temp_format(op_temp)
        
        for temp in op_temp_f: # check each of these permutations and add paranetheses
            if len(temp) > 0:
                if is_not_leading_0(op_temp):
                    # check for parentheses: if vector has len > 0 then we can append
                    paren_ls = check_paren(op_temp, inp)
    
        
        for op_temp in op_temp_f: # go through and compute
            if len(op_temp) > 0:
                if is_not_leading_0(op_temp): # if splitting doesn't result in leading 0s
                    int_split_temp = split_int(op_temp, inp) # get the split integers
                    int_val = compute_int_val(int_split_temp, op_temp) # compute the integer result
                    if compute_pass(int_val): # if it passes then we can check it against existing results
                        # see if it doesn't already exist; if so, then add all elements
                        if int_val_all.count(int_val) == 0:
                            int_val_all.append(int_val)
                            int_order_all.append(int_split_temp)
                            op_perm_all.append(op_temp)
                        else: # it does exist, so compare # of operations
                            val_index = int_val_all.index(int_val)
                            op_temp_original = op_perm_all[val_index]
                            if len(op_temp) < len(op_temp_original): # if we can use fewer # of operations, then replace the entry
                                op_perm_all[val_index] = op_temp
                                int_order_all[val_index] = int_split_temp
                            elif len(op_temp) == len(op_temp_original): # if same length, then if new order matches order in year, choose that
                                if inp == input_ls:
                                    op_perm_all[val_index] = op_temp
                                    int_order_all[val_index] = int_split_temp


        

# call the main driver function-----------------
def run():
    # for inp in input_perm:
    inp = input_perm[0]
    for p_ls in p_perm:
        update(p_ls, inp)


run()


tf = time.time()
print('Compute time = %.3fs' % (tf-t0))
