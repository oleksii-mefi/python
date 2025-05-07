def main():
    print("Програма для обчислення суми цифр тризначного числа")
    try:
        number = int(input("Введіть тризначне число: "))
        if 100 <= number <= 999:
            a = number // 100  # сотні
            b = (number // 10) % 10  # десятки
            c = number % 10  # одиниці
            total = a + b + c
            print(f"Сума цифр: {total}")
        else:
            print("Помилка: введене число не є тризначним.")
    except ValueError:
        print("Помилка: введіть ціле число.")


if __name__ == "__main__":
    main()
