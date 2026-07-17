class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        left = 0
        curr_sum = 0
        freq = {}
        for right in range(len(nums)):
            curr_sum += nums[right]
            freq[nums[right]] = freq.get(nums[right], 0) + 1

            if right - left + 1 > k:
                # window too big
                curr_sum -= nums[left]
                freq[nums[left]] -= 1
                
                # remove the number from hashmap
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                    
                left += 1
            
            # check if its a valid answer
            if right - left + 1 == k and len(freq) == k:
                ans = max(ans, curr_sum)
        return ans
                
        