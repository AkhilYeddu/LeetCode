import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.findall(r"\w+", paragraph.lower())
        freq = {}
        ans = ""
        ansLength = 0
        for word in words:
            if word not in freq:
                freq[word] = 1
            else:
                freq[word] += 1
        banned = set(banned)
        for key,value in freq.items():
            if value > ansLength and key not in banned:
                ans = key
                ansLength = value
        return ans

        
        


        
