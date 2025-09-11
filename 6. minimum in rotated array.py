'''
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
- sorted in assending order
- `nums` all unique element
- rotated `1-n` times
- must write `O(log n)` algorithm

## observation
- we need to search one element. but according to the property that the element is min
- and the array is said tobe sorted. although it is rotated.

- rotating n times !!! doesn't actually maintain it's sorted property
- iterative approach will take O(n).
- heapify or any sorting will take O(nlogn) at least. so it's a tough desicion if you don't know right pattern
- if you know the pattern we can. if not you can't

- looking at the input size n=5000, we can actually build O(n) solution.
- and the iterative approach is passed .

- but let's learn the algorithm

## Read carefully
- observing the example actually the array is not rotated n times
- what do they mean is n numerbers are rotated.
- viewing given few examples it seems like array is only `left-ratated`.
- numbers from right are put to the left. --- but not sure

### observation
- iterating over processes always brings something good
1. we find the mid.
2. compare to figure out sorted portion either left or right.
3. if left portion is sorted. why to search again in sorted portion
- leftmost in the sorted portion will be the min as array is sorted

(fact : only left-ratated)
if the right portion is sorted can you always say `mid` will be the min??
- No. [1, 2, 3, 4, 5, 6, 7] -> [6, 7, 1, 2, 3, 4, 5]
- lowest is above the mid point.
- so to solve this can't we just iterate to the left from mid  (fact : as only one rotation)
- unlit we find any missmatch (something greater.) and that is our ans

- but the thing is whenever iteration comes. test case can be organised to expoit it
- make the algo a O(n/2) or O(n)
- and with binary search it is confirmed that it will not take more than O(logn)

'''
#%%
class Solution:
    def findMin(self, nums: list[int]) -> int:
        ans = float('inf')
        low, high = 0, len(nums)-1
        while low<=high:
            mid = (low+high)//2
            if nums[mid]<=nums[high]:
                # right half is sortd
                ans = min(ans, nums[mid])
                high = mid -1
            else:
                # left half must be sorted
                ans = min(ans, nums[low])
                low = mid +1

        return ans

s = Solution()
# %%
s.findMin([4,5,6,7,0,1,2])
# %%
s.findMin([3,4,5,1,2])
# %%
s.findMin([11,13,15,17])
# %%
