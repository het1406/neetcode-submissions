class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        ran_dict , mag_dict = {},{}

        for i in range(len(ransomNote)):
            ran_dict[ransomNote[i]] = ran_dict.get(ransomNote[i],0) + 1
        for j in range(len(magazine)):
            mag_dict[magazine[j]] = mag_dict.get(magazine[j], 0) + 1

        count = 0

        for l in ran_dict:
            k = ran_dict[l]
            if k <= mag_dict.get(l,0):
                count+=1
            else: 
                return False 
        return count == len(ran_dict)