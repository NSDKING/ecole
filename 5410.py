reponse = input("Entrez un nombre de lignes (entier positif): ")
N = int(reponse)

for i in range(1, N + 1):
    if i <= 4:
        print('*' * (2 * i - 1))
    else:
        print('* ' * (2 * i - 1))