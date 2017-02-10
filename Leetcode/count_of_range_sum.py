def countRangeSum(nums, lower, upper):
    """
    :type nums: List[int]
    :type lower: int
    :type upper: int
    :rtype: int
    """
    
    nums_size = len(nums)
    count = 0
    sum = 0
    print ("list size is ",nums_size)
    for i in range(0,nums_size):
        if(nums[i] >= lower and nums[i] <= upper):
            count = count + 1
            print("first pass for index ",i)
    
    if(nums_size >= 2):
        sum = nums[0]
        for i in range(1,nums_size):
            sum = sum + nums[i]
            if(sum >= lower and sum <= upper):
                count = count + 1
                print("second pass for index ",i)
    
    return (count)


nums=[-2,5,-1]
lower=-2
upper=2
print(countRangeSum(nums,lower,upper))
print("\n\n")
nums=[0,0]
lower=0
upper=0
print(countRangeSum(nums,lower,upper))
print("\n\n")
nums=[2147483647,-2147483648,-1,0]
lower=-1
upper=0
print(countRangeSum(nums,lower,upper))