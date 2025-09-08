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
'''