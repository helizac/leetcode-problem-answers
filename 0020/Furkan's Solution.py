class Solution(object):
    def isValid(self, s):
        while len(s) > 0:
            l = len(s)
            s = s.replace("()","")
            s = s.replace("[]","")
            s = s.replace("{}","")
            if l == len(s):
                return False
        return True
