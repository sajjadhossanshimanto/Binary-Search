# https://leetcode.com/problems/search-insert-position/description/
'''
# Question
- sorted array
- distinct integers
- *KEY* :  finding in a sorted array -> is binary search


# theory
- upder bound | lower bound
    - a slight modification to binary search.
    - instade of searching for exact match as in normal binary search
    - here we will match for greater or lower 

## Lower bound
inp -> nums:[], ele:int
return -> the smallest index such that `nums[and] >= ele`

## Upper bound
smallest index such that `nums[ans] > ele`

## cheat
    [1, 2, 3, 4, 5, 6, 7, 8] ele=5
    - possible cheat : find the element. the next index after that pos is ans
    -  but what if the element is not in that list is `upper bound`

    - upper limit is actually nothing but [bst_index+1]
'''
#%%
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1


        # return -1 
        """
        nums = [1,3,5,6], target = 2
        ans = 1
        what will be our l&r when we didn't find out ?
        
        """
        return r+1

s = Solution()
#%%
p = s.searchInsert(nums = [1,3,5,6], target = 2)
p = s.searchInsert(nums = [1,3,5,6], target = 7)


print(p)
# %%
#  TODO: implement lower bound
