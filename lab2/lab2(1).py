def triangle(x, a, b, c):
    if x <= a or x >= c:
        return 0
    elif a <= x <= b:
        return (x - a) / (b - a)
    elif b < x <= c:
        return (c - x) / (c - b)

# Введення параметрів
try:
    a = float(input("Введіть a (a < b < c): "))
    b = float(input("Введіть b: "))
    c = float(input("Введіть c: "))

    if not (a < b < c):
        raise ValueError("Потрібно, щоб a < b < c")

    # Вивід значень функції на діапазоні [a-1, c+1] з кроком 0.5
    print("\nЗначення функції triangle(x; a, b, c):")
    x = a - 1
    while x <= c + 1:
        y = triangle(x, a, b, c)
        print(f"x = {x:.2f}, μ(x) = {y:.2f}")
        x += 0.5

except ValueError as e:
    print("Помилка:", e)
