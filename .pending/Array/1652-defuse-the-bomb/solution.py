class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        l=[]
        if k==0:
            l= [0]*len(code)
        elif k>0:
            x=code.pop(0)
            code.append(x)
            s=0
            for i in range(k):
                s+=code[i]
            l.append(s)
            for i in range(len(code)-1):
                s=s-code[0]+code[0+k]
                l.append(s)
                x=code.pop(0)
                code.append(x)
        else:
            s=0
            o=len(code)
            for i in range(o+k,o):
                s+=code[i]
            l.append(s)
            x=code.pop(0)
            code.append(x)
            for i in range(o-1):
                s=s-code[k-1]+code[-1]
                x=code.pop(0)
                code.append(x)
                l.append(s)

        return l
                
      