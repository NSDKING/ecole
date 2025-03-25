
def cos(x):
    n=1
    sum = 1
    prev_sum=0
    while (sum-prev_sum)>10**(-4):
        prev_sum=sum
        un = (((-1)**n)*(x**(2*n)))/factoriel((2*n))
        sum+=un
        n+=1
    return sum
 
def factoriel(n):
    k=1
    for i in range(1,n+1):
            k*=i
    return k


x=3.149939
print(f'cos({x})={cos(x)}')    
 

 
     

    