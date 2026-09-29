X = float(input("X (|X|<1): "))
N = int(input("N: "))
total = 0.0
current_pow = 1.0
for i in range(1, N + 1):
    current_pow *= X
    if i % 2 == 1:
        total += current_pow / i
    else:
        total -= current_pow / i
print(total)