'''
18. 4Sum (+)
https://leetcode.com/problems/4sum/
'''

class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        res = []
        i = 0
        while i < len(nums) - 3:
            j = i + 1
            while j < len(nums) - 2:
                left = j + 1
                right = len(nums) - 1
                ans = target - nums[i] - nums[j]
                while left < right:
                    if nums[left] + nums[right] > ans:
                        right -= 1
                    elif nums[left] + nums[right] < ans:
                        left += 1
                    else:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                while j < len(nums) - 2 and nums[j] == nums[j + 1]:
                    j += 1
                j += 1
            while i < len(nums) - 3 and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        return res