'''
912. Sort an Array
https://leetcode.com/problems/sort-an-array/description/
'''

# Функция слияния двух массивов
def merge(l_, r_):
    mass = []
    i = 0
    j = 0
    while i < len(l_) and j < len(r_):
        if l_[i] <= r_[j]:
            mass.append(l_[i])
            i += 1
        else:
            mass.append(r_[j])
            j += 1

    mass += l_[i:] + r_[j:]
    return mass


class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Сортировка подсчетом
        m = min(nums)
        mass = [0] * (max(nums) - m + 1)
        res = []
        for x in nums:
            mass[x - m] += 1
        for i in range(len(mass)):
            res += [i + m] * mass[i]
        return res

        # Сортировка слиянием
        left = nums[:len(nums) // 2]
        right = nums[len(nums) // 2:]

        if len(left) > 1:
            left = Solution.sortArray(self, left)
        if len(right) > 1:
            right = Solution.sortArray(self, right)

        return merge(left, right)

        # Быстрая сортировка
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        menshe = []
        center = []
        bolshe = []
        for item in nums:
            if item < nums[mid]:
                menshe.append(item)
            elif item > nums[mid]:
                bolshe.append(item)
            else:
                center.append(item)
        return Solution.sortArray(self, menshe) + center + Solution.sortArray(self, bolshe)
