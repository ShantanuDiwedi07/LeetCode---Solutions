class Solution(object):
    def dailyTemperatures(self, temperatures):
        result = [0]*len(temperatures)
        stack =  []
        for i , temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<temp :
                idx = stack.pop()
                result[idx] = i-idx
            stack.append(i)
        return result 