def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
        res=[]
        def dfs(total,i,cur):
            if target==total:
                res.append(cur.copy())
                return 
            if i >= len(candidates) or total>target:
                return
            cur.append(candidates[i])
            dfs(i,cur,total+candidates[i])
            cur.pop()
            dfs(i+1,cur,total)
        dfs(0,0,[])
        return res
if __name__=='__main__':
    print(combinationSum([2,3,6,7],7))