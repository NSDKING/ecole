fibo = [0, 1]

for i in range(2, 15):
    fibo.append(fibo[i-1] + fibo[i-2])

print("Les 15 premiers termes de la suite de Fibonacci sont:")
print(fibo)

print("\nRapports entre les termes consécutifs (n > 1):")
for i in range(2, 15):
    rapport = fibo[i] / fibo[i-1]
    print(f"fibo[{i}] / fibo[{i-1}] = {rapport}")

print("L! rapport tend vers la constante: Le nombre d'or (environ 1.618)")