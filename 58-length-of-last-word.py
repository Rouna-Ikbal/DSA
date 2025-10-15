# Example 1:

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
# Example 2:

# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
# Example 3:

# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.


def lengthOfLastWord( s: str) -> int:
    end = len(s)-1  #get the last index
    while s[end] == " ":   #find ending index of last word
        end -= 1
        
    start = end
    while start >= 0 and s[start] != " ":  #find beginning index of last word
        start -= 1
    return end - start  #return length of last word
    

print(lengthOfLastWord("   fly me   to   the moon  "))