class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        difference = {}
        min_diff = float(inf)
        for i in range(1, len(arr)):
            value = abs(arr[i-1] - arr[i])
            min_diff = min(min_diff, value)
            if value not in difference:
                difference[value] = []
            difference[value].append([arr[i-1], arr[i]])
        return difference[min_diff]