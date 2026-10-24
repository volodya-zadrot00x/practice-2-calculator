print("=== Консольный калькулятор ===")
print("Доступные операции: +, -, *, /, //, %, ^")
print()

while True:
    # Ввод первого числа
    while True:
        try:
            first_number = float(input("Введите первое число: "))
            break
        except ValueError:
            print("Ошибка! Введите корректное число.")

    # Ввод операции
    while True:
        operation = input(
            "Введите операцию (+, -, *, /, //, %, ^): "
        ).strip()

        if operation in ["+", "-", "*", "/", "//", "%", "^"]:
            break
        else:
            print("Ошибка! Неизвестная операция. Попробуйте ещё раз.")

    # Ввод второго числа
    while True:
        try:
            second_number = float(input("Введите второе число: "))
            break
        except ValueError:
            print("Ошибка! Введите корректное число.")

    # Выполнение вычисления
    if operation == "+":
        result = first_number + second_number
    elif operation == "-":
        result = first_number - second_number
    elif operation == "*":
        result = first_number * second_number
    elif operation == "/":
        if second_number == 0:
            print("Ошибка! Делить на ноль нельзя.")
            result = None
        else:
            result = first_number / second_number
    elif operation == "//":
        if second_number == 0:
            print("Ошибка! Делить на ноль нельзя.")
            result = None
        else:
            result = first_number // second_number
    elif operation == "%":
        if second_number == 0:
            print("Ошибка! Делить на ноль нельзя.")
            result = None
        else:
            result = first_number % second_number
    elif operation == "^":
        result = first_number ** second_number

    # Вывод результата
    if result is not None:
        print("Результат:", result)

    print()

    # Проверка желания продолжить работу
    while True:
        answer = input(
            "Хотите выполнить ещё одну операцию? (да/нет): "
        ).strip().lower()

        if answer == "да":
            print()
            break
        elif answer == "нет":
            print("Работа программы завершена.")
            break
        else:
            print("Ошибка! Введите 'да' или 'нет'.")

    if answer == "нет":
        break