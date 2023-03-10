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
from more_itertools import locate # get all locations of particular value in list
from sympy import solve, simplify # for solving string equations; for dealing with complex numbers
from sympy.abc import x
from sympy.parsing.sympy_parser import parse_expr
from joblib import Parallel, delayed # for paralellization
import multiprocessing
from tqdm import tqdm # to give progress bars

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
input='2022'
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

# now figure out possible operations, the integers to be used in the calcultations, and the final answer
# for the first two, we use list of list of tuples; for the value, just list of lists of integer
op_perm_all = []
int_order_all = []
int_val_all = []


# function to build  equation in strings
def build_eq(int_split_temp, op_temp):
    # print(int_split_temp)
    # print(op_temp)
    eqn = ""
    split_index = 0
    a = 0
    while a < len(op_temp):
        op = op_temp[a]
        # print('a', a)
        # print('op', op)
        
        if op==0: # if hit 0, keep going until no more 0s
            # print('hjer')
            for b in range(a+1, len(op_temp), 1):
                # print(split_index)
                if (op_temp[b] != 0) or ((op_temp[b] == 0) and (b==len(op_temp)-1)):
                    if split_index < len(int_split_temp):
                        eqn+=str(int_split_temp[split_index])
                        split_index+=1
                    a+=(b-(a+1))
                    break
                    # print('a here', a)
        else:
            eqn+=str(op_dict[str(op)])
            if a == len(op_temp)-1: # if at the end, add the opreation and then the digit
                if split_index < len(int_split_temp):
                    eqn+=str(int_split_temp[split_index])
                break
            
            if op != -3 and op_temp[a+1]!=0:
                # if (op == -2) or (op_temp[a+1] == -2): # if we have open paren (
                if op ==-2:
                    eqn+=str(op_dict[str(op_temp[a+1])])
                    # a+=1
                    
                if split_index < len(int_split_temp):
                    eqn+=str(int_split_temp[split_index])
                    split_index+=1
                a+=1
            else:
                # print('here')
                # if next one is 0, keep going until we run out of the 0s
                for b in range(a+1, len(op_temp), 1):
                    if (op_temp[b] !=0) or ((op_temp[b] == 0) and (b==len(op_temp)-1)):
                        # print('split', split_index)
                        if split_index < len(int_split_temp):
                            eqn+=str(int_split_temp[split_index])
                            split_index+=1
                        a+=(b-(a+1))
                        break
        a+=1
            
    return eqn
 # note to actually solve this need to add 'x=' to beginning and call the compute function


# custom function to calculate operation perms
def update(p_ls, inp): # takes in current p list and input numbers
    # op_total = [] # finalized list of all formatted op_temps
    # int_order_temp = [] # list to hold integers broken up by operations
    # int_val_temp = [] # list to hold computations for the integers and the operations
    # op_temp_f_all = [] # list to hold all formatted op temps, including parenthese
    def temp_format(op_temp): # nested function to format the op_temps from [(2), (1, 2, 3, 4, 5), (0)] => [(2, 1, 0), (2, 2, 0), etc]
        
        # get count of full operations lists; this determines the r value for permutations
        r = op_temp.count(operations)
        # print(r)
        if r > 0:
            temp_all = []
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
        else:
            print(op_temp)
            temporary = [op[0] for op in op_temp]
            temp_all = []
            temp_all.append(temporary)
        # print('temp all', temp_all)
        return temp_all

    # helper function to compute string representation of split integers
    
    def parse_split_str(op_temp, inp):
        int_split_str = [] # list to hold split integers as strings
        # don't care about parentheses so remove them
        op_temp_cleaned = []
        for op in op_temp:
            if not(op in [-2, -3]):
                op_temp_cleaned.append(op)

        op_temp = op_temp_cleaned
        op_int = 0
        while op_int < len(op_temp):
            temp_split = ''
            current_op = op_temp[op_int]
            # next_op = op_temp[op_int+1]
            # if current_op ==0: # if it's 0, figure out how many more 0s so inp values to keep appending
            temp_split+=str(inp[op_int])
            for op_next_int in range(op_int+1, len(op_temp), 1):
                next_op = op_temp[op_next_int]
                
                if (op_next_int == len(op_temp)-1):
                    if next_op==0:
                        temp_split+=str(inp[op_next_int])
                        int_split_str.append(temp_split)
                    else:
                        int_split_str.append(temp_split)
                        int_split_str.append(str(inp[op_next_int]))
                    op_int+=(op_next_int-op_int)
                    break
                elif next_op == 0:
                    temp_split+=str(inp[op_next_int])
                else: # it's not 0
                    int_split_str.append(temp_split)
                    op_int+=(op_next_int-op_int)-1
                    break
            # else:
            #     temp_split+=str(inp[op_int])
            #     int_split_str.append(temp_split)
            
            op_int+=1

        return int_split_str

    def is_not_leading_0(op_temp, inp): # call function to check if no leading 0s; if true, then call int_split
        int_split_str = parse_split_str(op_temp, inp)
        #print(int_split_str)
        for int_split in int_split_str:
            #print(int_split[0])
            if (int_split[0]=='0') and (len(int_split) > 1): # if first index is 0 of multicharacter integer, then return false: i.e. there IS a leading 0
                #print('false')
                return False
        return True # if we haven't returned False, it must be True

    # def not_divide_0(int_split_ls, op_temp):
    #     for int_split in int_split_ls:
    #         if int_split==0:


    def check_paren(op_temp): # function to return a list of parenthesis variations
        # initialize parentheses list
        # print('op_temp', op_temp)
        op_paren = []
        # subfunction to check ok'd prior characters
        def get_paren_temp(op_index_ls, ok_ls):
            for index in op_index_ls:
                for s in range(index-1, -1, -1):
                    if op_temp[s] in ok_ls: # if the character is in ok list, add to paren list
                        op_paren_temp = [op for op in op_temp]
                        op_paren_temp.insert(index, -3) # add closing paren
                        op_paren_temp.insert(s, -2) # add opening paren
                        op_paren.append(op_paren_temp) # add result to op_paren list
        # we need to compute op_indices lists for *, /, ^ and do check ok separately
        # for * and /, ok list includes +, -, ^
        multi_divide_ok = [1, 2, 5]
        # for ^, we get +, -, *, /
        exp_ok = [1, 2, 3, 4]
        mult_index_ls = list(locate(op_temp, lambda x: x==3))
        divide_index_ls = list(locate(op_temp, lambda x: x==4))
        exp_index_ls = list(locate(op_temp, lambda x: x==5))

        # check for *, /, ^
        if len(mult_index_ls) >= 1:
            get_paren_temp(mult_index_ls, multi_divide_ok)
        if len(divide_index_ls) >=1:
            get_paren_temp(divide_index_ls, multi_divide_ok)
        if len(exp_index_ls) >=1:
            get_paren_temp(exp_index_ls, exp_ok)

        return op_paren # return the final list


    def split_int(op_temp, inp): # asssumes not leading 0
        int_split_str = parse_split_str(op_temp, inp)
        int_split_int = [] # new list to hold the integer versions
        for int_split in int_split_str:
            int_split_int.append(int(int_split))
        return int_split_int

    def compute_int_val(int_split_temp, op_temp):
        eqn = build_eq(int_split_temp, op_temp)
        eqn = "x="+eqn
        #print(eqn)
        # the code below in this function is adapted from https://stackoverflow.com/questions/30775453/converting-a-string-into-equation-and-resolve-it
        try:
            lhs =  parse_expr(eqn.split("=")[0])
            rhs =  parse_expr(eqn.split("=")[1])
            value = solve(lhs-rhs)[0]
            #print(value)
            return value
        except:
            #print("invalid equation:", eqn)
            return -1 # return a value that will get filtered out by compute_pass

    # function to count op number; don't count -2 or -3
    def count_num_ops(op_temp):
        c = 0 # initialize count
        for op in op_temp:
            if (op != -2) and (op != -3) and (op != 0): # if not ( or ), then increment count
                c+=1
        return c
    
    def compute_pass(int_val):
        if simplify(int_val).is_real:
            return ((int(int_val) - int_val == 0) and (int_val >= 1) and (int_val <= 100)) # conditions stated in problem
        else:
            return False # not real, so not integer
    def compute_all(op_temp):# go through and compute
            # print(op_temp)
            if len(op_temp) > 0:
                if is_not_leading_0(op_temp, inp): # if splitting doesn't result in leading 0s
                    # print('not leading 0', op_temp)
                    int_split_temp = split_int(op_temp, inp) # get the split integers
                    int_val = compute_int_val(int_split_temp, op_temp) # compute the integer result
                    
                    # display results in real time
                    eqn = build_eq(int_split_temp, op_temp)
                    print(str(int_val) + ' = ' + eqn)

                    if compute_pass(int_val): # if it passes then we can check it against existing results
                        # print('compute pass', op_temp)
                        # see if it doesn't already exist; if so, then add all elements
                        if int_val_all.count(int_val) == 0:
                            int_val_all.append(int_val)
                            int_order_all.append(int_split_temp)
                            op_perm_all.append(op_temp)
                        else: # it does exist, so compare # of operations
                            val_index = int_val_all.index(int_val)
                            op_temp_original = op_perm_all[val_index]
                            current_num_ops = count_num_ops(op_temp)
                            original_num_ops = count_num_ops(op_temp_original)
                            if current_num_ops < original_num_ops: # if we can use fewer # of operations, then replace the entry
                                op_perm_all[val_index] = op_temp
                                int_order_all[val_index] = int_split_temp
                            elif current_num_ops < original_num_ops: # if same length, then if new order matches order in year, choose that
                                if inp == input_ls:
                                    op_perm_all[val_index] = op_temp
                                    int_order_all[val_index] = int_split_temp
                            # else if it's bigger, then don't do anything -- keep original
                # else:
                #     print('has leading 0s')
    # want only unique
    p_ls = list(set(p_ls))
    #print(p_ls)
    for p_tuple in p_ls:
        # print(p_tuple)
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
        # print('before', op_temp_f)
        # print(op_temp_f[0])
        
        paren_ls_ls = [] # list to store list of paren lists
        for op_f in op_temp_f: # check each of these permutations and add paranetheses
                # print(op_f)
                # print(len(op_f))
                if len(op_f) > 0:
                    #print('here')
                    if is_not_leading_0(op_f, inp):
                        #print('getting paren')
                        # check for parentheses: if vector has len > 0 then we can append
                        #print(op_temp)
                        paren_ls = check_paren(op_f)
                        if len(paren_ls) > 0:
                            paren_ls_ls.append(paren_ls)
            

        # now go through all paren_ls and append to op_temp_f
        for paren_ls in paren_ls_ls:
            for paren_temp in paren_ls:
                op_temp_f.append(paren_temp)
        # print('here')
        #print(len(op_temp_f))
        # since this is where we actually do all the computaytion, we will want to parallelize here
        
        # call parallelization
        # num_cores = multiprocessing.cpu_count()
        # Parallel(n_jobs=num_cores)(delayed(compute_all)(op_temp) for op_temp in op_temp_f)
        
        # non-parallelized
        for op_temp in op_temp_f:
            compute_all(op_temp)
        # print('done with parallelization')

# function to output the results
def print_results():
    def first(t):  
        return t[0]    
     
    # function to sort the tuple     
    def sort(tuple_ls):  
        return sorted(tuple_ls, key = first)  
    
    # take all 3 lists, zip them together, then sort
    results = list(zip(int_val_all, int_order_all, op_perm_all))
    results_sorted = sort(results)
    
    
    print('Found %i solutions:' %len(int_val_all))
    for result in results_sorted:
        int_val = result[0]
        int_split = result[1]
        op_temp = result[2]
        eqn = build_eq(int_split, op_temp)
        print(str(int_val) + ' = ' + eqn)

# call the main driver function-----------------
def run():
    for inp in tqdm(input_perm, desc='progress on input...', position=0):
    #inp = input_perm[0]
        for p_ls in p_perm:
            # update(p_ls, inp)
            print('updated')

    # now call printing function for each value in the op_perm_all, int_order_all, and int_val_all
    print('-----------------------')
    print_results()


run()


tf = time.time()
print('Compute time = %.3fs' % (tf-t0))
