class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack1 = []
        result = []

        for i in range(len(temperatures)):
            result.append(0)
            while stack1 and  temperatures[i] > temperatures[stack1[-1]]:
                x = stack1.pop()
                result[x] = i - x
            stack1.append(i)
        return result 




    
            


        