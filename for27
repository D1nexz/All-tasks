X = float(input("X (|X|<1): "))
N = int(input("N: "))
total = X
current_term = X
for i in range(1, N + 1):
    # Переход к следующему члену: умножаем на (2i-1)^2 * X^2 / (2i * (2i+1))
    current_term *= ((2 * i - 1)**2 * X * X) / ((2 * i) * (2 * i + 1))
    total += current_term
print(total)