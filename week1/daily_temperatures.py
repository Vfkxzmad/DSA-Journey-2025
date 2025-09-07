class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        s=[]
        k=[0]*n
        for i,t in enumerate(temperatures):
            while s and t>s[-1][1]:
                ind,temp=s.pop()
                k[ind]=i-ind
            s.append((i,t))
        return k
