# Example 1:

# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.
# Example 2:

# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

def mySqrt( x: int) -> int:
    if x==0 or x ==1:
        return x
    else:
        l = 1
        r = x // 2
        while l <= r:
            m = (l+r)//2
            sqr = m * m
            if sqr == x:    #if square is x then res is m
                return m
            elif sqr < x:
                l = m + 1
                res = m         # number can less but not more than x
            else:
                r = m - 1
        return res
        
#time complexity is O(logn)
#space complexity is O(1)

print(mySqrt(8))