# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.


def threeSum( nums: list[int]) -> list[list[int]]:
    #two pointer 
    #O(n^2)
    #first sort the array to use twosum-II method. 
    # uses  two loops - one for first element , second for two pinters -> l , r
    #choose first element , check if its repeated/duplicates - if the current element is same as previous element then that array starting with same value will be duplicate.
    # then apply binary search method - two pointers  
    # then in that check whether left element is duplicate or not before appending to result array.
    # here increment 2nd number if number is less than 0, when storing result and if the moved left is the same as stored left. 
    nums.sort()
    res = []
    n = len(nums)
    for i in range(n):
        if (i > 0 and nums[i] == nums[i-1]):
            continue
        left, right = i+1, n-1
        while (left < right):
            threeSum = nums[i] + nums[left] + nums[right]
            if (threeSum) > 0: #greater value, then reduce 
                right -= 1
            elif (threeSum) < 0: #small value, then move to greater number
                left += 1 
            else:
                res.append([nums[i],nums[left],nums[right]])   #append the result array
                left += 1 
                #check if 2nd number is repeating to avoid duplicate array. ie,
                #[-1,0,1], [-1,-1,2], here 1st element and 2nd element we check if repeated,
                while(nums[left] == nums[left-1] and left < right):         
                    left += 1                           
                                
    return res

print(threeSum([-1,0,1,2,-1,-4]))
    