def two_sum(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i
    return None
print(two_sum(nums=[2, 7, 11, 15], target=9))
print(two_sum(nums=[3, 2, 4], target=6))
##