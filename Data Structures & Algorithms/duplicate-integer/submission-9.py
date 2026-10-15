class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupl_list = []
        for i in nums:
            if i not in dupl_list:
                dupl_list.append(i)

            else:
                return True
        return False
        