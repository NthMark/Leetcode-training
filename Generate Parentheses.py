def generateParenthesis(self, n: int) -> list[str]:
        stack=[]
        res=[]
        def backtrack(nOpen,nClosed):
            if nOpen==nClosed==n:
                res.append(''.join(stack))
            if nOpen <n:
                stack.append('(')
                backtrack(nOpen+1,nClosed)
                stack.pop()
            if nClosed <nOpen:
                stack.append(')')
                backtrack(nOpen,nClosed+1)
                stack.pop()
        backtrack(0,0)
        return res