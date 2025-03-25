error = float(input("enter the error:"))
n=1
sum=1
prev_sum=0
while abs(sum-prev_sum)>error:
    prev_sum=sum
    un = ((-1)**n)/(2*n+1)**2
    sum = un+sum
    n=n+1
print(sum)
