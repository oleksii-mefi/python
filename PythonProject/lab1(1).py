def calculate_density(mass, volume):
    if volume == 0:
        raise ValueError("Об'єм не може дорівнювати нулю.")
    return mass / volume


def main():
    print("Програма для обчислення густини матеріалу")
    try:
        mass = float(input("Введіть масу тіла (г): "))
        volume = float(input("Введіть об'єм тіла (см³): "))
        density = calculate_density(mass, volume)
        print(f"Густина матеріалу: {density:.2f} г/см³")
    except ValueError as e:
        print(f"Помилка: {e}")

if __name__ == "__main__":
    main()

