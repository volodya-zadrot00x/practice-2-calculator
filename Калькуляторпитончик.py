print("=== Консольный калькулятор ===")
print("Доступные операции: +, -, *, /, //, %, ^")
print()
while True:
    try:
        first_number = float(input("Введите первое число: "))
        break
    except ValueError:
        print("Ошибка! Введите корректное число.")
while True:
    operation = input(
        "Введите операцию (+, -, *, /, //, %, ^): "
    )
    if operation in ["+", "-", "*", "/", "//", "%", "^"]:
        break
    else:
        print("Ошибка! Неизвестная операция. Попробуйте ещё раз.")
while True:
    try:
        second_number = float(input("Введите второе число: "))
        break
    except ValueError:
        print("Ошибка! Введите корректное число.")
if operation == "+":
    result = first_number + second_number
    print("Результат:", result)
elif operation == "-":
    result = first_number - second_number
    print("Результат:", result)
elif operation == "*":
    result = first_number * second_number
    print("Результат:", result)
elif operation == "/":
    if second_number == 0:
        print("Ошибка! Делить на ноль нельзя.")
    else:
        result = first_number / second_number
        print("Результат:", result)
elif operation == "//":
    if second_number == 0:
        print("Ошибка! Делить на ноль нельзя.")
    else:
        result = first_number // second_number
        print("Результат:", result)
elif operation == "%":
    if second_number == 0:
        print("Ошибка! Делить на ноль нельзя.")
    else:
        result = first_number % second_number
        print("Результат:", result)
elif operation == "^":
    result = first_number ** second_number
    print("Результат:", result)