def nod(a, b):
    """
    Вычисляет наибольший общий делитель (НОД) двух чисел.
    """
    while b != 0:
        a, b = b, a % b
    return a

def mod_obrat(a, m):
    """
    Находит модулярное обратное к a по модулю m.
    Использует расширенный алгоритм Евклида.
    """
    if nod(a, m) != 1:
        return None  # Обратное существует только если a и m взаимно просты

    # Инициализация переменных
    x_prev, x_curr = 1, 0
    y_prev, y_curr = 0, 1
    m_orig = m  # Сохраняем исходное значение m

    while m != 0:
        q = a // m  # Частное
        a, m = m, a % m  # Обновляем a и m
        # Обновляем коэффициенты
        x_prev, x_curr = x_curr, x_prev - q * x_curr
        y_prev, y_curr = y_curr, y_prev - q * y_curr

    # Возвращаем x_prev, приведённое по модулю m_orig
    return x_prev % m_orig

def affine_recurrent_shifr(text, a1, a2, b1, b2, alph):
    """
    Шифрует текст с использованием аффинного рекуррентного шифра.
    """
    shifr_text = ""
    m = len(alph)
    a_prev, a_curr = a1, a2  # Инициализация ключей a
    b_prev, b_curr = b1, b2  # Инициализация ключей b
    for symbol in text:
        if symbol in alph:
            x = alph.index(symbol)  # Символ в виде числа
            y = (a_curr * x + b_curr) % m  # Шифрование
            shifr_text += alph[y]
            # Обновление ключей
            a_next = (a_curr * a_prev) % m
            b_next = (b_curr + b_prev) % m
            a_prev, a_curr = a_curr, a_next
            b_prev, b_curr = b_curr, b_next
        else:
            shifr_text += symbol  # Оставляем символы, не входящие в алфавит
    return shifr_text

def affine_recurrent_deshifr(text, a1, a2, b1, b2, alph):
    """
    Дешифрует текст, зашифрованный аффинным рекуррентным шифром.
    """
    deshifr_text = ""
    m = len(alph)
    a_prev, a_curr = a1, a2  # Инициализация ключей a
    b_prev, b_curr = b1, b2  # Инициализация ключей b
    for symbol in text:
        if symbol in alph:
            y = alph.index(symbol)  # Символ в виде числа
            a_obr = mod_obrat(a_curr, m)  # Обратное к a_curr по модулю m
            if a_obr is None:
                return "Ошибка: ключ 'a' и размер алфавита не взаимно просты."
            x = a_obr * (y - b_curr) % m  # Дешифрование
            deshifr_text += alph[x]
            # Обновление ключей
            a_next = (a_curr * a_prev) % m
            b_next = (b_curr + b_prev) % m
            a_prev, a_curr = a_curr, a_next
            b_prev, b_curr = b_curr, b_next
        else:
            deshifr_text += symbol  # Оставляем символы, не входящие в алфавит
    return deshifr_text

def main():
    """
    Основная функция программы.
    """
    russian_alph = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    english_alph = "abcdefghijklmnopqrstuvwxyz"

    # Запрос данных у пользователя
    language = input("Выбери язык (русский или английский): ").strip().lower()
    mode = input("Выбери режим (шифрование или дешифрование): ").strip().lower()
    text = input("Введи текст: ").strip().lower()
    a1 = int(input("Введи начальный ключ 'a1': "))
    a2 = int(input("Введи начальный ключ 'a2': "))
    b1 = int(input("Введи начальный ключ 'b1': "))
    b2 = int(input("Введи начальный ключ 'b2': "))

    # Выбор алфавита
    if language in ["русский", "рус"]:
        alph = russian_alph
    elif language in ["английский", "англ"]:
        alph = english_alph
    else:
        print("Неа, выбери другой язык.")
        return

    # Выбор режима
    if mode in ["шифрование", "шифр"]:
        result = affine_recurrent_shifr(text, a1, a2, b1, b2, alph)
        print("Зашифрованный текст:", result)
    elif mode in ["дешифрование", "дешифр"]:
        result = affine_recurrent_deshifr(text, a1, a2, b1, b2, alph)
        print("Расшифрованный текст:", result)
    else:
        print("Ошибка, неправильный режим.")

if __name__ == "__main__":
    main()