class Solution(object):
    def backspaceCompare(self, s, t):
        stack1=[]
        stack2=[]
        len1= len(s)
        len2= len(t)
        for i in range (len1):
            if s[i]=="#":
                if stack1 == []:
                    continue
                else:
                    stack1.pop()
            else :
                stack1.append(s[i])
        for i in range (len2):
            if t[i]=="#":
                if stack2 == []:
                    continue
                else:
                    stack2.pop()
            else :
                stack2.append(t[i])
        if stack1==stack2:
            return True 
        else :
            return False 