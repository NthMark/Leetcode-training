def longestPalindrome( s: str) -> str:
        "90 / 142 testcases passed"
        s=[x for x in s]
        maxlen=0
        maxsubstring=[]
        if len(s)==1:
            return s[0]
        for step in range(len(s)):
            for j in range(len(s)):
                if j+step+1>len(s):
                    break
                backward=s[j:j+step+1]
                backward.reverse()
                if backward==s[j:j+step+1]:
                    if maxlen<len(backward):
                        maxlen=len(backward)
                        maxsubstring=backward
        return ''.join(maxsubstring)
def longestPalindromeOPtimalSolution(s: str) -> str:
        "All testcases passed"
        res=""
        resLen=0

        for i in range(len(s)):
            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>resLen:
                    res=s[l:r+1]
                    resLen=r-l+1
                l-=1
                r+=1
            
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>resLen:
                    res=s[l:r+1]
                    resLen=r-l+1
                l-=1
                r+=1
        return res
if __name__=='__main__':
    s=""
    print(longestPalindromeOPtimalSolution(s))