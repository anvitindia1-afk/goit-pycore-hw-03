# Завдання 2: випадкові неповторні числа для лотереї.

# Підключаємо модуль для випадкових чисел
import random


def get_numbers_ticket(min, max, quantity):
    """
    Повертає відсортований список із quantity різних випадкових чисел
    від min до max (включно).
    Якщо параметри неправильні, повертає порожній список [].
    """
    # Перевіряємо умови: min не менше 1, max не більше 1000,
    # min менше за max, і чисел у проміжку вистачає на quantity штук
    if min < 1 or max > 1000 or min > max:
        return []
    if quantity < 1 or quantity > (max - min + 1):
        return []

    # Множина (set) сама прибирає повтори
    numbers = set()
    while len(numbers) < quantity:
        numbers.add(random.randint(min, max))

    # sorted() робить із множини відсортований список
    return sorted(numbers)


if __name__ == "__main__":
    lottery_numbers = get_numbers_ticket(1, 49, 6)
    print("Ваші лотерейні числа:", lottery_numbers)

    print(get_numbers_ticket(1, 36, 5))
    print(get_numbers_ticket(0, 49, 6))   # min менше 1 — буде []
    print(get_numbers_ticket(1, 10, 20))  # чисел замало — буде []
