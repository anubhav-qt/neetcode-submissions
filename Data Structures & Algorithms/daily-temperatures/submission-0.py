class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        res = [0] * length
        stack = []

        for index, temperature in enumerate(temperatures):
            while stack and stack[-1][0] < temperature:
                t, i = stack.pop()
                res[i] = index - i
            
            stack.append((temperature, index))

        return res
