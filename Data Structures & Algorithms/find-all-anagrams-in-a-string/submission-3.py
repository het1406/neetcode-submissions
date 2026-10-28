class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        output =[]
        p_dict = {}
        for char in p:
            p_dict[char] = p_dict.get(char,0) + 1

        
        x = s[0:len(p)]
        s_window_dict = {}
        for char in x:
            s_window_dict[char] = s_window_dict.get(char,0) + 1

        left = 0 
        right = len(p) - 1 
        while right < len(s):
            if p_dict == s_window_dict:
                output.append(left)
            if right == len(s) - 1:
                break 
            s_window_dict[s[left]] -= 1
            if s_window_dict[s[left]] == 0:
                del s_window_dict[s[left]]
            s_window_dict[s[right+1]] = s_window_dict.get(s[right+1], 0) + 1

            left+=1 
            right+=1

        return output 
