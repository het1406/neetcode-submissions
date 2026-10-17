class Solution:
    def firstUniqChar(self, s: str) -> int:
        tracker = {}

        for i in range(len(s)):
            k = s[i]
            tracker[k] = tracker.get(k,0) + 1


        for j in tracker:
            if tracker[j] == 1:
                return s.index(j) 
        return -1
            
        