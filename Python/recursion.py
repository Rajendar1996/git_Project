l=[-1]*101
l2=[]
def nth_fib(n=100):
    if(n==0 or n==1):
        return n
    if(l[n]!=-1):
        return l[n]
    x=nth_fib(n-1)
    y=nth_fib(n-2)
    l[n]=x+y
    return l[n]
def gen_subsets(string, start=0, res=""):
    l2.append(res)
    
    for i in range(start, len(string)):
        # choose
        res += string[i]
        
        # explore
        gen_subsets(string, i+1, res)
        
        # un-choose (backtrack)
        res = res[:-1]

gen_subsets("abc")
print(nth_fib(),l)
print(l2)
