class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(p1, p2, nums):
            while p1 < p2:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p1 += 1 
                p2 -= 1
        k  = k % len(nums) # rotating 7 times is same as rotating 2 times
        reverse(0, len(nums) - 1, nums)
        reverse(0, k - 1, nums)
        reverse(k, len(nums)-1, nums)
        return nums
        