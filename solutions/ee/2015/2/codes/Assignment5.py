from random import randint

# Given set A={2,3,4,5} and B={11,12,13,14,15}
# Let x is the number selected randomly from ser A
# Let y is the number selected randomly from set B

num = 1000000
n = 0
count = 0

while n<num:
    x = randint(2,5)
    y = randint(11,15)
    sum = x+y
    if sum==16:
        count = count+1
    
    n = n+1

prob = count/num
print("Probability that the sum of the numbers is 16 is ",prob)