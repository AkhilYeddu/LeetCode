class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hashmap = {}
        res = []
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1

        for key in hashmap.keys():
            if hashmap[key] > 1:
                res.append(key)
           
        return res
            
        
        