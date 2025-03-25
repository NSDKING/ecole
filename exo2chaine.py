def sum_digit(nbr):
    sum=0
    for i in list(nbr):
        sum+=int(i)
    return sum

def multi_digit(nbr):
    sum=1
    for i in list(nbr):
        sum*=int(i)
    return sum

def is_diviseur(a,b):
    if a%b==0:
        return(True)
    else:
        return False
    
def check(nbr):
    sum = sum_digit(str(nbr))
    multi = multi_digit(str(nbr))

    return is_diviseur(multi,sum)

n = 100
while n<=999:
    if(check(n)):
        print(n)
    n+=1
