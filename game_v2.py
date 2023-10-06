"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """_summary_

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
    return count


def binar_predict(number: int = 1) -> int:
    """_summary_

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    low = 1
    high = 101
    while low <= high:
        count += 1
        mid = (low + high) / 2
        if number == mid:
            break  # выход из цикла если угадали
        elif number > mid:  # если угадываемое значение больше среднего значения диапазона
            low = mid + 1  # задаем нижнее значение диапазона по среднему значению предыдущей итерации
        else:  # если угадываемое значение меньше среднего значения диапазона
            high = mid - 1  # задаем верхнее значение диапазона по среднему значению предыдущей итерации
    # Ваш код заканчивается здесь
    return count


def score_game(predict_alg) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        predict_alg ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    # np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=1000)  # загадали список чисел

    for number in random_array:
        count_ls.append(predict_alg(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
    score_game(binar_predict)
