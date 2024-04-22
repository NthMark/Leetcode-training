def lengthOfLongestSubstring(s: str) -> int:
        "986 / 987 testcases passed"
        s=[x for x in s]
        maxlen=0
        if len(s)==1:
            return 1
        if len(s)==0:
            return 0
        for step in range(len(s)):
            for j in range(len(s)):
                if j+step+1>len(s):
                    break
                count=set(s[j:j+step+1])
                if maxlen <len(s[j:j+step+1]) and len(count)==len(s[j:j+step+1]):
                    maxlen=len(s[j:j+step+1])
        if maxlen == 0:
            maxlen=len(s)
        return maxlen
def lengthOfLongestSubstringOptimalSolution(s: str) -> int:
        "All testcases passed"
        
        charset=set()
        l=0
        res=0
        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l+=1
            charset.add(s[r])
            print(charset)
            res=max(res,r-l+1)
        return res
if __name__=='__main__':
    s="abcabcbb"
    print(lengthOfLongestSubstringOptimalSolution(s))