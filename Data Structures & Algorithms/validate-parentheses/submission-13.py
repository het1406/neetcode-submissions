class Solution:
    def isValid(self, s: str) -> bool:
        dict1 = {']':'[', '}':'{', ')':'('}
        list1 = []

        for i in s:
            if i in dict1:
                if len(list1) == 0:
                    return False
                elif list1[-1] != dict1[i]:
                    return False
                elif list1[-1] == dict1[i]:
                    list1.pop()

            
            else:
                list1.append(i)
        return len(list1) == 0   

            
        
      



        