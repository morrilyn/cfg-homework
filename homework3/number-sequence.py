# Write a function that returns the Nth number in the followng sequence- recursive solution 
"""write a function that returns Nth number in the following sequence 8, 15, 22, 29, 36
This is a arithemetic sequence where each number is 7 more than the previous one, starting with 8. The general formula for the nth term of an arithmetic sequence is a_n = a_1 + (n-1)d, where a_1 is the first term and d is the common difference."""
def number_sequence(n): 
    if n == 1: 
        return 8
    else: 
        return number_sequence(n-1) + 7
    
print(number_sequence(3))

# In recursive solution, we need to keep track of the previous number in the sequence.
# we can do this by passing it as an argument to the function.
# the base case is when n = 1, we return the first number in the sequence, which is 8
# otherwise, we return the previous number in the sequence plus 7

def number_sequence_recursive(n):
    if n == 1:
        return 8
    else:
        return number_sequence_recursive(n - 1) + 7

