def convert( s: str, numRows: int) -> str:
        "All testcases passed"
        nDiagonals=numRows-2
        nRows=numRows
        if nDiagonals<0:
            nDiagonals=0
        table=[]
        column=[]
        index=numRows-1
        isRestart=False
        isTransfer=False
        for i in range(len(s)):
            if nDiagonals==0 and isRestart:
                nRows=numRows
                nDiagonals=numRows-2
                index=numRows-1
                isRestart=False
            if nRows==0 and nDiagonals>0:
                index-=1
                column=[0]*numRows
                column[index]=s[i]
                table.append(column.copy())
                column.clear()
                nDiagonals-=1
                if nDiagonals==0:
                    isRestart=True
            if nRows>0:
                column.append(s[i])
                nRows-=1
                if nRows==0:
                    isTransfer=True
                    table.append(column.copy())
                    column.clear()
                if nDiagonals==0 and isTransfer:
                    isTransfer=False
                    nRows=numRows
                if i==len(s)-1:
                     column+=[0]*(numRows-len(column))
                     table.append(column.copy())
            
        res=[]
        print(table)
        if len(table)==1:
            res=s
        else:
            for j in range(numRows):
                for i in range(len(table)):
                    if table[i][j]!=0:
                        res.append(table[i][j])
        return ''.join(res)
if __name__=='__main__':
    s = "ABC"
    numRows = 2
    print(int('012'))