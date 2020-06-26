# Soren Sabet Sarvestany 
# March 5th 2019

# Given this sorted set of numbers:  {4, 8, 15, 16, 23, 42, 43, 44, 45, 46, 47, 48, 49}
# A function picks a random subset of size 6, and returns the minimum of that subset. 
# What is the expected value of this function? 

import numpy as np 
import math 
import random
import scipy
import itertools

# Theoretical calculation: 
# 13 numbers, so each one has 1/13 chance of being selected 
# Randomly selecting 6 numbers, so 6/13 chance of being selected for each iteration
# Largest five numbers (45,46,47,48,49) have a zero probability of being selected 
# Order doesn't matter, so we are interested in combination and not permutation 
# Number of ways to choose 6 numbers from 13 total numbers: 1716
# Not sure how to proceed...

# Brute force Method 1: 
# There are 1716 different combinations of 6 numbers of the above set. 
# Each subset has a mininum value equal to one of the numbers in the original set
# By calculating the min value for all 1716 different combinations, I can find the probability of each number being returned
# Then I calculate expected value by multiplying probability by the number 

nums = sorted({49, 8, 48, 15, 47, 4, 16, 23, 43, 44, 42, 45, 46})
num_combs = scipy.special.comb(len(nums), 6)

combinations = list(itertools.combinations(nums, 6))
freq_tracker = np.zeros([len(nums),2]) # Column 1 is number, Column 2 is number of times the number has shown up
freq_tracker[:,0] = nums
 
for comb in combinations: # Count the number of times each value shows up
    min_num = min(set(comb))
    freq_tracker[np.argwhere(freq_tracker[:,0] == min_num),1] += 1 
expected_value = np.sum(np.prod(freq_tracker, axis=1))/num_combs
print('The expected value for this problem is: ' + str(expected_value))