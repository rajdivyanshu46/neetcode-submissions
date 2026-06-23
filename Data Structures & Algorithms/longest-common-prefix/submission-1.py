class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1:
            return strs[0]
        def check(a,b):
            v = ""
            if len(a)>len(b):
                c = a
                d = b
            else:
                c = b
                d = a
            for i in range(len(d)):
                if d[i]!=c[i]:
                    return v
                else:
                    v+=d[i]
            return v
        q = check(strs[0],strs[1])
        for i in range(2,len(strs)):
            q = check(strs[i],q)
        
        return q



        