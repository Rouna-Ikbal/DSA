# Example 1:

# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example 2:

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 3:

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

def romanToInt( s: str) -> int:
    sum = 0
    d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    for i in range(len(s)):
        if (i != len(s)-1) and (d[s[i]] < d[s[i+1]]):
            sum -= d[s[i]]
            i += 2
        else:
            sum += d[s[i]]
    return sum

print(romanToInt("LVIII"))

#solution 1 -> O(n), O(1)
        # for i in range(len(s)):
        #     print (i,s[i],sum)
        #     if s[i] == 'I':
        #         sum += 1
        #     elif s[i] == 'V':
        #         if i>0 and s[i-1] == 'I':
        #             sum += (4-1)  #subtract the previously added value 1
        #         else:
        #             sum += 5
        #     elif s[i] == 'X':
        #         if i>0 and s[i-1] == 'I':
        #             sum += (9-1)
        #         else:
        #             sum += 10
        #     elif s[i] == 'L':
        #         if i>0 and s[i-1] == 'X':
        #             sum += (40-10)
        #         else:
        #             sum += 50
        #     elif s[i] == 'C':
        #         if i>0 and s[i-1] == 'X':
        #             sum += (90-10)
        #         else:
        #             sum += 100
        #     elif s[i] == 'D':
        #         if i>0 and s[i-1] == 'C':
        #             sum += (400-100)
        #         else:
        #             sum += 500
        #     elif s[i] == 'M':
        #         if i>0 and s[i-1] == 'C':
        #             sum += (900-100)
        #         else:
        #             sum += 1000

        # return sum
