'''
https://leetcode.com/problems/search-in-rotated-sorted-array/
## key point
- sorted in assending order
- distinct values
- left rotated (spacified) -> one rotation
- 0 indexing
- return -1 if not present

## algo
- we need to search 
- and the array is sorted
so it might be solved by binary search

## Approach
- my first tought was -> as we can't apply the normal binary serch
- 1st find the pos where it is rotated then apply binary search individually
- and we can find the rotating point with binary search as well
- by comparing `mid` with `left` and `right`
- where `left < mid` & `right > mid`
- if any of the rule is violated then the rotation point exits in that portion.
- and we can eliminate the sorted porstion.

but it turns out we can actually search while looking for the rotational point
reducing the time complexity.
- as we are eliminating the sorted half. why not to check for the existing of traget 
- as this portion is confirmed tobe sorted

'''

#%%
def binary_search(nums, target, low, high):
    # check the out of change in main function
    # so if it returns -1 that means target doesn't exits

    while low<=high:
        mid = (low+high)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]>target:
            high = mid - 1
        else:
            low = mid + 1
    
    return -1


class Solution:
    def search(self, nums, target: int) -> int:
        if not nums: return -1

        low, high = 0, len(nums)-1

        while low<=high:
            mid = (low+high)//2
            if nums[mid]==target:
                return mid
            elif nums[mid] < nums[low]: 
                # mis condition in lower half
                search_range = mid, high
                high = mid-1
            else:
                search_range = low, mid
                low = mid+1
            
            if nums[search_range[0]]<=target and target<=nums[search_range[1]]:
                return binary_search(nums, target, *search_range)
            
        return -1


s= Solution()
#%%
s.search(nums = [4,5,6,7,0,1,2], target = 0)# ans: 4
#%%
s.search( nums = [4,5,6,7,0,1,2], target = 3)# ans: -1
# %% wa 
s.search([1,3], 1)
# ans: 0 
# got: -1

# %% wa
# binary_search([3, 5, 1], 3, 0, 2)
s.search(nums=[3, 5, 1], target=3)
# %% wa
s.search([4,5,6,7,0,1,2], 0)
# %%
