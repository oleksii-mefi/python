import math

def main():
    print("Програма для обчислення периметра та діагоналі прямокутника")
    try:
        a = float(input("Введіть довжину першої сторони (a): "))
        b = float(input("Введіть довжину другої сторони (b): "))

        perimeter = 2 * (a + b)
        diagonal = math.sqrt(a**2 + b**2)

        print(f"Периметр прямокутника: {perimeter:.2f}")
        print(f"Довжина діагоналі: {diagonal:.2f}")
    except ValueError:
        print("Помилка: введіть числові значення для сторін.")

if __name__ == "__main__":
    main()
