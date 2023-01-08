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
operations = list(range(1, 5, 1))

input = str(input('Enter a year (e.g., 2023)'))
# convert to list of integers
input_ls = [int(c) for c in input]

t0 = time.time() # start the clock

input_perm = list(permutations(input_ls)) # get permutations of input number





tf = time.time()
print('Compute time = %.3fs' % (tf-t0))
