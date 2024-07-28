class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        def spec(n):
            c=0
            for i in range(1,n+1):
                if(n%i==0):
                    c+=1
            return(c==2)
        p=0
        for i in range(l,r+1):
            if(not spec(i)):
                print(i)
                p+=1  
        return (p) 
    
o1=Solution()
print(o1.nonSpecialCount(4,16))