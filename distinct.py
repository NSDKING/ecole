def is_distinct(number):
    number_list= list(number)
    distinct = False
    nbr=number_list[0]
    for i in number_list:
        if(nbr != i):
            distinct=True
            break
        else:
            nbr=i
    return distinct

print(is_distinct("10"))

