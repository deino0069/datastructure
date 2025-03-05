def bubbleSorting(nums): # Function: Used to perform bubble sorting.
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
            
nums = [4,3,2,16,7,9,21,4,12,32,1]

bubbleSorting(nums)
print(f'Result: {nums}')
