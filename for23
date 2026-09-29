X = float(input("X: "))
N = int(input("N: "))
total = 0.0
current_term = X
for i in range(1, N + 1):
    total += current_term
    # Переход к следующему члену: умножаем на -X^2 / ((2i)*(2i+1))
    current_term *= -X * X / ((2 * i) * (2 * i + 1))
print(total)