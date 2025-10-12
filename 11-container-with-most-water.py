# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1


def maxArea( height: list[int]) -> int:
    # area = height x width = [left] x (right-left) or [right] x (right - left)
    # h = min(h1,h2) = min ([left],[right])
    # width = right - left
    maxArea = 0
    l = 0
    r = len(height) - 1
    while(l<r):
        area = (min(height[l],height[r])) * (r-l)
        if (height[l]> height[r]):
            r -= 1
        else:
            l += 1
        maxArea = max (maxArea,area)
    return maxArea
    
print(maxArea([1,8,6,2,5,4,8,3,7]))