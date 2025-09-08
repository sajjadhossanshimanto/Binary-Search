'''
https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
- return `bool` -> exists or not
- necessarily with `distinct` values
that is the main difference from I

now the question is what is the problem with repeated element
nums = [1, 2, 3, 3, 3, 3, 4, 5, 6]
(after rotation) -> [3, 3, 4, 5, 6, 1, 2, 3, 3]

while our mid = 6 both the left and right is 3
here we can't say left is sorted or right is sorted
thereby can't eleminate any portion.

## solve
the trick is we will trim left or right as long as they match with other side 
or mid point

'''

#%%
def binary_search(nums, target, low, high):
    # check the out of change in main function
    # so if it returns -1 that means target doesn't exits

    while low<=high:
        mid = (low+high)//2
        if nums[mid]==target:
            return True
        elif nums[mid]>target:
            high = mid - 1
        else:
            low = mid + 1
    
    return False


class Solution:
    def search(self, nums, target: int) -> bool:
        if not nums: return False

        low, high = 0, len(nums)-1

        while low<=high:
            mid = (low+high)//2
            while nums[high]==nums[mid] and mid<high:
                # so at lower high will be equal to mid
                high -= 1
            
            while nums[low]==nums[mid] and low<mid:
                # so at max low will be equal to mid
                low += 1
            
            # if nums[mid]==target:
            #     # i think mid check will obiously be done in `binary_search` function
            #     # no mater which part is sorted mid point will be passed to search
            #     return True
            if nums[mid]>nums[high]:
                # lower part is sorted
                if binary_search(nums, target, low, mid): 
                    return True
                low = mid + 1
            else:
                if binary_search(nums, target, mid, high): 
                    return True
                high = mid - 1
        
        return False

s = Solution()
# %%
s.search(nums = [2,5,6,0,0,1,2], target = 0)
# %%
s.search(nums = [2,5,6,0,0,1,2], target = 3)
# %%
