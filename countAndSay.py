def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        seq=[1]
        newseq=[]
        for _ in range(1,n):
            count=[]
            l=0
            substr=[]
            for r in range(len(seq)):
                if seq[r]!=seq[l]:
                    count.append((len(seq[l:r]),seq[l]))
                    l=r
                
                if r==len(seq)-1 and seq[r]==seq[l]:
                    count.append((len(seq[l:r+1]),seq[l]))
            for i in range(len(count)):
                newseq.append(count[i][0])
                newseq.append(count[i][1])
            seq=newseq[:]
            newseq.clear()
        seq=[str(x) for x in seq]
        return ''.join(seq)