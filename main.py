# Calculate the sum of the digits of a random three-digit number using indexes

import random
ran_dig = str(random.randint(100, 999)) #random digit [100,999]
print(ran_dig)
n = int(ran_dig[0])  #digit - first position - index 0
m = int(ran_dig[1])  #digit - first position - index 1
k = int(ran_dig[2])  #digit - first position - index 2
print(n+m+k)         #sum of 3 digits

