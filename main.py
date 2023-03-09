def twoSum(self, nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        if(i + 1 <= len(nums)):
                if nums[i] + nums[i + 1] == target:
                    ans = [i, i + 1]
                    return ans