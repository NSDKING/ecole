n=1
x = 5
sum = 1
prev_sum=0
while x> 1 or x<-1 :
    x = float(input("entre un nbre entre -1 et 1: "))

def factoriel(n):
    k=1
    for i in range(1,n):
        k*=i
    return k


while (sum-prev_sum)<10**(-4):
    prev_sum=sum
    un = (((-1)**n)*(x**(2*n)))/factoriel((2*n))
    sum+=un
    n+=1

print(factoriel(10))
    

    