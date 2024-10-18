from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    result = []  # save elements
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            temp = nums[i] + nums[j]
            if temp == target: # check the value
                result.append(i) # list update
                result.append(j)

    return result