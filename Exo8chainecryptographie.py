def crypto(chaine:str):
    char:str=chaine[0]
    Res:str=""
    occ:int=0
    for i in chaine: 
        if i == char:
            occ+=1
        else:
            Res += str(occ)+char
            char=i
            occ=1
    return Res

print(crypto("kkkkkkkkkkkkkkkkkkkklmmmmmmmmmmmmp_________")) 