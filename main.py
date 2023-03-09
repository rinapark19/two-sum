from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        if(i + 1 <= len(nums)):
                if nums[i] + nums[i + 1] == target:
                    ans = [i, i + 1]
                    return ans