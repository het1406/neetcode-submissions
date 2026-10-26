class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapstot , mapttos = {},{}
        for i in range(len(s)):
            c1, c2 = s[i], t[i]
            if (c1 in mapstot and mapstot[c1] != c2) or (c2 in mapttos and mapttos[c2]!=c1):
                return False
            mapstot[c1] = c2
            mapttos[c2] = c1

        return True 
        