
# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

def twoSum( nums: list[int], target: int) -> list[int]:        
    prev_map = dict()
    for i, num in enumerate(nums):
        if ((target - num) in prev_map):
            return (prev_map[target-num],i)
        prev_map[num] = i
    
    return -1
            
print(twoSum([2,7,11,15],9))
        