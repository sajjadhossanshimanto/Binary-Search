# https://leetcode.com/problems/binary-search/ 
# solved 
'''
To NOTE:
- array must be sorted
- 

# code
- l and r are inclusive
```
[-1,0,3,5,9,12]
target = 13
```
- as the target is out of tange 
- we can implement a half open interval [l, r)
```
l, r = 0, len(nums)   # notice r = len, not len-1
while l < r:
    mid = (l+r)//2
    if nums[mid] < target:
        l = mid+1
    else:
        r = mid
```


# complexity
- at each stage the array is trimed into half
- so the at most iteration is log2(N). 
'''

from typing import List

#%% iterative -> 0ms
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (r+l)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                r = mid - 1
            else:
                l = mid + 1
        return -1

#%% recursive -> 0ms 100%
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def search(l, r):
            if r>l: return -1
            
            mid = (r+l)//2
            if nums[mid]==target:
                return mid
            elif nums[mid] > target:
                return search(l, mid-1)
            elif nums[mid] < target:
                return search(mid+1, r)
            
            return -1
        
        return search(0, len(nums)-1)

#%% cheat
'''
as the array is not actually too large
- just 10^4. we can use the iterative approach as well
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except Exception:
            return -1