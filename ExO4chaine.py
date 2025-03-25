#this function add digits forming a number using power 
def add_digit_with_power(nbr:int,pow:int):
    nbr_converted = str(nbr)
    liste= list(nbr_converted)
    sum=0
    for i in liste:
        sum+=int(i)**pow
    return sum    

#do the things that was ask in the exercise
def does_it_work(nbr:int):
    is_it=False
    n=0
    for i in range(1,6):
        if nbr == add_digit_with_power(nbr,i):
            is_it=True
            n=i
    print(f'{is_it} {n}')
    return is_it    

does_it_work(2114)

