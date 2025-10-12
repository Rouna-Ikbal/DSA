# Given two integers a and b, return the sum of the two integers without using the operators + and -.

# Example 1:

# Input: a = 1, b = 2
# Output: 3
# Example 2:

# Input: a = 2, b = 3
# Output: 5



def getSum( a: int, b: int) -> int:
    #here we check the sum without carry
    #we also check the carry
    #then move the carry to left and then again check the sum
    #then again check the carry
    #and repeat untill we have zero carry
    #can replace b or the 2nd number with carry after first check so that we can add it.
    #eg:
    # sum = a ^ b
    # carry = a & b
    #left shist the carry to left and add with the existing sum to reach till end
    # ie; a = sum and b = carry << 1
    MASK = 0xFFFFFFFF   # to make 2's complememt 1111 1111 1111 1111 1111 1111 1111 1111 
    MAX = 0x7FFFFFFF #maximum 32bit positive numbers, 111 1111 1111 1111 1111 1111 1111 1111
    while (b != 0):
        carry = (a & b) & MASK
        a = (a ^ b) & MASK      #sum = a^b => next a
        b = (carry << 1) & MASK
    if a <= MAX:     #if positive number
        return a
    else:
        return ~(a ^ MASK)
        #to ensure we stay within 32 bits, we have to perform & MASK on all steps in the loop, or else the bits keep shifting.
    # while (b != 0):
    #     carry = a & b
    #     a = a ^ b       #sum = a^b => next a
    #     b = carry << 1                                                                                                                                                                                                                                   


print(getSum(2,3))
print(getSum(-1,1))
print(getSum(-4,-5))