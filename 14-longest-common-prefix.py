# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

def longestCommonPrefix( strs: list[str]) -> str:
    #take the first word and compare it with other strings in the list
    #compare using the length of letters in common and set it.
    #start from first word
    prefix = strs[0]
    #get the length
    prefix_len = len(strs[0])
    #start from the 2nd word.s[0]<->s[1], s[0]<->s[2]
    for s in strs[1:]:
        while prefix != s[0:prefix_len]:
            prefix_len -= 1
            if prefix_len == 0:  #if reached zero length then o prefix
                return ""
            prefix = prefix[0:prefix_len] #refuce the length of prefix unntil it matches
    return prefix

print(longestCommonPrefix(["flower","flow","flight"]))