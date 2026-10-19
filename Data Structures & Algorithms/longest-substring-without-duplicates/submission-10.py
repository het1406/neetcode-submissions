class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_string = ''
        max_sub_string = ''
        for i in range(len(s)):
            current_char = s[i]
            if current_char not in sub_string:
                sub_string += current_char
                
            else:
                sub_string = sub_string[sub_string.index(current_char)+1:]
                sub_string += current_char
            if len(sub_string) > len(max_sub_string):
                max_sub_string = sub_string
                
        return len(max_sub_string)


        