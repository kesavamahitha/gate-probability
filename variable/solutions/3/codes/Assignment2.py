def Prob_set(x):
    " This function gives us the probability of the variable being in the interval of (0,x]"
    if (x>= 0) and (x< 1/2):
        return x/2
    if (x>= 1/2) and (x<= 1):
        return x
    else:
        print("The variable sample space is smaller than the given set")

def Prob_element(x):
    "This function gives the probability of the variable being a particular element x"
    return Prob_set(x) - Prob_set(x - 0.000000000001)
print("The probability of the variable being 1/2 calculated by simulation is:",Prob_element(1/2))
print("The probability of the variable being 1/2 calculated theorotically is: 0.25")
print("The error in  calculation of probability by simulation is:",Prob_element(1/2) - 0.25)
  