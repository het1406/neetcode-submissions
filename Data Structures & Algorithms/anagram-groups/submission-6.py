class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list2 = ["".join(sorted(i)) for i in strs]  # Sorted form of each word
        outputlist1 = []
        seen = set()  # To avoid duplicate groups

        for m, n in enumerate(list2):
            if n in seen:
                continue
            seen.add(n)
            group = [strs[i] for i, x in enumerate(list2) if x == n]
            outputlist1.append(group)

        return outputlist1