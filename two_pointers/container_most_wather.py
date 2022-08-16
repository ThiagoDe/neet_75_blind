height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# Output: 49

def maxArea(height): #linear time solution O(n)
    res = 0
    l, r = 0, len(height) - 1

    while l < r:
        area = (r - l) * min(height[l], height[r]) # area cal r - l * min height
        res = max(area, res)
        if height[l] > height[r]:
            r -= 1
        else:
            l += 1

    return res 

print(maxArea(height))