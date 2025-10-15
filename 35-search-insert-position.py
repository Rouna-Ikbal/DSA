# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4

def searchInsert( nums: list[int], target: int) -> int:
       l=0
       r=len(nums)-1
       while(l<r):
           m = (l+r)//2
           if(target == nums[m]):
               return m
           elif(target > nums[m]):
               l = m + 1
           else:
               r = m - 1
       if (nums[l] < target ):
           return l+1
       else:
           return l
       
print(searchInsert([1,3,5,6], 5))
       