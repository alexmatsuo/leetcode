def TwoSum(nums,target):
    i = 0
    current = nums[0]
    while i < len(nums):
        j = i + 1
        while  j < len(nums):
            sum = current + nums[j]
            if sum == target :
                return i,j
            j += 1
        i += 1
        current = nums[i]

result = TwoSum([3,2,3], 6)
print(result)