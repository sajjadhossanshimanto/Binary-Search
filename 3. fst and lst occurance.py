'''
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
- search in sorted array -> manei binary search



## prolem is 1st and last index of target

- 1st index -> obiously the most efficient way to find one is bst
- lst index -> bst from the other side ??

## cheat
- as the array is sorted all the similar numbers should be one after another
- can't we just iterate until we find mitchmatch
'''
#%%
from typing import List


#%% 
'''
notmal binary search can't guranty the pos of 1st occurance
as the mid point might be any occurrence of the target, not necessarily the first one.
it only confirms eithget the target exists or not
'''
def bst_index(num, target):
    if not num: return -1

    # optimisation -> as the array is sorted
    if target<num[0] or target>num[-1]:
        return -1
    
    low, high = 0, len(num)-1# low - inclusive; high - exclusive
    while low<=high:
        mid = (low+high)//2
        if num[mid]==target:
            return mid
        elif num[mid]>target:
            high = mid - 1
        elif num[mid]<target:
            low = mid + 1
    
    return -1

#%% lower limit
'''
the smallest index that is >= target
important to NOTICE:
-> smallest
-> greatr or equal

## to ensure smallest
- we will the return imidiately after finding a match 
- we will store that pos as `ans` and try to minimise as long as we can
- when we will reach our boundery we will return the `ans` variable

## here
- for this problem we will ignore `greater` 
- and will only look for `exact` match

'''
def lower_limit_bst(num, target):
    if not num: return -1

    # optimisation -> as the array is sorted
    if target<num[0] or target>num[-1]:
        return -1

    ans = -1 
    '''
    initial value of `ans` could have been ln(num), if we consider `greater` than
    as the last index is obiously greater than the target.
    but we need to minimise the `ans`.
    '''
    low, high = 0, len(num)
    while low<=high:
        mid = (low+high)//2
        if num[mid]==target:
            ans = mid
            high = mid - 1
        elif num[mid]>target:
            high = mid - 1
        elif num[mid]<target:
            low = mid + 1
    
    return ans

#%%
def upper_limit_bst(num, target):
    if not num: return -1
    if target < num[0] or target > num[-1]:
        return -1

    ans = -1
    low, high = 0, len(num) - 1
    while low <= high:
        mid = (low + high) // 2
        if num[mid] == target:
            ans = mid
            low = mid + 1
        elif num[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return ans

#%%
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        fst_idx = lower_limit_bst(nums, target)
        if fst_idx==-1:
            return -1, -1
        
        """for finding the last poshere we could have implemented 
            we could have implemented another bst sarching for the last index of occurance
            but time complexity would be the same

            in worse case:
            our iterative approach -> need to iterate the whole array to find the last index 
            that is O(N)
            but with binary search will it be log(n) max 🤔
        """
        cur = fst_idx
        while cur<len(nums) and nums[cur]==nums[fst_idx]:
            cur+=1
        
        return fst_idx, cur-1

s = Solution()
#%%
s.searchRange(nums = [], target = 0)
# %%
s.searchRange(nums = [5,7,7,8,8,10], target = 8)
# %%
s.searchRange(nums = [5,7,7,8,8,10], target = 6)
# %%
