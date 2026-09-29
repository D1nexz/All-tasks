X = float(input("X (|X|<1): "))
N = int(input("N: "))
total = 0.0
current_pow = X
for i in range(1, N + 1):
    if i % 2 == 1:
        total += current_pow / (2 * i - 1)
    else:
        total -= current_pow / (2 * i - 1)
    current_pow *= X * X
print(total)