def add_digit(nbr):
    nbr_converted = str(nbr)
    liste= list(nbr_converted)
    sum=0
    for i in liste:
        sum+=int(i)
    return sum

def is_autonombre(nbre):
    is_it=True
    for i in range(nbre):
        sum = i + add_digit(i)
        if nbre==sum:
            is_it=False
    return is_it     

print(is_autonombre(20))    