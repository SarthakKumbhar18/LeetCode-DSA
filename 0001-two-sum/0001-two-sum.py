class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:


        res = [-1,-1]

        d = {}

        for i in range(0,len(nums)):
            if(target - nums[i]  in d):
                res[0] = d[target-nums[i]]
                res[1] = i
                return res

            else:
                d[nums[i]] = i
        return res
        