import re
from typing import Callable, Generator

# Аналізує текст та повертає генератор дійсних чисел (доходів), які чітко відокремлені пробілами.
# INPUT text: рядок для аналізу
# OUTPUT yields: дійсне число, знайдене у тексті
def generator_numbers(text: str) -> Generator[float, None, None]:
    
    # Варіант 1 - регулярний вираз фільтрує числа
    pattern = r"\s(-?\d+\.?\d*)\s"
    matches = re.findall(pattern, text)
    # генеруємо числа зі знайдених патернів
    for match in matches:
        try:
            yield float(match)
        except ValueError:
            # ця помилка малоймовірна, оскільки регулярний вираз вже фільтрує числа
            print(f"Увага: знайдено недійсне число: '{match}'")
            
    # # Варіант 2 - без використання регулярних виразів
    # parts = text.split()
    # for part in parts:
    #     try:
    #         yield float(part)
    #     except ValueError:
    #         # Якщо частина не є дійсним числом, ігноруємо її
    #         pass

# # Перевірка роботи генератора
# text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід,
#         доповнений додатковими надходженнями 27.45 і 324.00 доларів."
# gen = generator_numbers(text)
#
# print(next(gen)) # 1000.01
# print(next(gen)) # 27.45
# print(next(gen)) # 324.0


# Використовує генератор generator_numbers для обчислення загальної суми чисел у вхідному рядку
# та приймає його як аргумент при виклику
# INPUT text: рядок, що містить числа.
#       func: функція-генератор, яка приймає рядок і повертає генератор чисел.
# OUTPUT загальна сума дійсних чисел у тексті
def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    total_profit = 0.0
    # складаємо усі згенеровані числа з тексту
    for number in func(text):
        total_profit += number
    # повертаємо загальний дохід з округленням до другого знаку після крапки
    return round(total_profit, 2)

# Приклад використання:
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}") # Загальний дохід: 1351.46

