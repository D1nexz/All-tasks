X = float(input("X (|X|<1): "))
N = int(input("N: "))
total = 1.0
current_term = 1.0
for i in range(1, N + 1):
    # Переход к следующему члену: умножаем на -(2i-3)*X / (2i)
    # Для i=1: множитель -(-1)*X/2 = X/2. Для i=2: -1*X/4 и т.д.
    multiplier = -(2 * i - 3) * X / (2 * i)
    current_term *= multiplier
    total += current_term
print(total)