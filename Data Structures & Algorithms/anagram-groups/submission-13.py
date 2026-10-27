class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {} 
        for i in strs:
            x = ''.join(sorted(i))
            if x in group:
                group[x].append(i)
            else:
                group[x] = [i]
        return list(group.values())