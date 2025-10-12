# Example 1:

# Input: x = 121
# Output: true"
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

def isPalindrome( x: int) -> bool:
    if (x < 0):
        return False
    else:
        r = 0
        num = x
        while num != 0:
            r = (r * 10) + (num % 10)
            num = num//10
        if (x == r):
            return True
        else:
            return False
    #another solution
    # x = str(x)
	# return x == x[::-1]

print(isPalindrome(-121))