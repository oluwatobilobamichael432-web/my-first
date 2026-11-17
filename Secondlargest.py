def secondlarge(nums):
    largest = nums[0]
    second = nums[0]

    for num in nums:
        if num > largest :
            second = largest
            largest = num
        if largest > num > second:
            second = num
            return second
print(secondlarge([4, 9, 2, 9, 7, 9]))
