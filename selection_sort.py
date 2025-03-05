def selectionSorting(nums): #  Function: Used to perform selectionSorting.
    for i in range(len(nums)):
        minpos = i
        for j in range(i,6):
            if nums[j] < nums[minpos]:
                minpos = j

    
        nums[i],nums[minpos] = nums[minpos],nums[i]
    
    return nums



nums = [6,44,32,2,90,5,43]
print(selectionSorting(nums))

