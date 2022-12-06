'''
2418. Sort the People
https://leetcode.com/problems/sort-the-people/description/
'''

class Solution(object):
    def compare(self, item1, item2):
        if item1[0] < item2[0]:
            return 1
        elif item1[0] > item2[0]:
            return -1
        else:
            if item1[1] < item2[1]:
                return 1
            elif item1[1] > item2[1]:
                return -1
            else:
                return 0


    def quick_sort(self, lst):
        if len(lst) < 2:
            return lst
        mid = len(lst) // 2
        left, center, right = [], [], []
        for item in lst:
            check = Solution.compare(self, item, lst[mid])
            if check == 1:
                right.append(item)
            elif check == -1:
                left.append(item)
            else:
                center.append(item)
        return Solution.quick_sort(self, left) + center + Solution.quick_sort(self, right)


    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        lst = []
        for i in range(len(names)):
            lst.append((heights[i], names[i]))
        lst = Solution.quick_sort(self, lst)
        return [x[1] for x in lst]