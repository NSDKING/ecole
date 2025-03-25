def exo(nbre:int):

    if nbre>100:
        strnbre:str = str(nbre)
        somme:int = 0
        for i in strnbre:
            somme +=int(i)
        
        while somme>9 or somme<1:
            som:int = somme
            for i in str(somme):
                
