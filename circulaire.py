def is_premier(nbr:int):
    is_it:bool =True
    for i in range(2,nbr):
        if nbr%i ==0:
            is_it=False
            break
    return is_it

def circule (nbr:int):
    nbr:str = str(nbr)
    circule_list = []
    for i, char in enumerate(nbr):
        circule = nbr[i:] + nbr[:i] 
        circule_list.append(circule)
    return circule_list
    
def is_circulaire(nbr:int):
    is_it:bool =True
    for i in circule(nbr):
        if is_premier(int(i))==False:
            is_it=False
            break
    return is_it

def nbre_circulaire(p:int,q:int):
    circule_list = []
    for i in range(p,q+1):
        if is_circulaire(i):
            circule_list.append(i)
    return circule_list

print(nbre_circulaire(0,10000))