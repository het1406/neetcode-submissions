class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        morphic_dict = {} 
        list1 = morphic_dict.values()

        for i in range(len(s)):
            if s[i] not in morphic_dict and t[i] not in list1:
                morphic_dict[s[i]] = t[i]
           
            elif morphic_dict.get(s[i],'') != t[i]:
                return False 
        return True 

