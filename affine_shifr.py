def nod(a, b):
    while b != 0:
        a, b = b, a % b  # a на b, а b на остаток от деления a/b
    return a

def mod_obrat(a, m):
    if nod(a, m) != 1:
        return None  # обратное существует только если a и m взаимно простые
    x_prev, x_curr = 1, 0
    y_prev, y_curr = 0, 1
    m_orig = m
    while m != 0:
        q = a // m
        a, m = m, a % m
        x_prev, x_curr = x_curr, x_prev - q * x_curr
        y_prev, y_curr = y_curr, y_prev - q * y_curr
    return x_prev % m_orig

def affine_shifr(text, a, b, alph):
    shifr_text = ""
    m = len(alph)
    for symbol in text:
        if symbol in alph:
            x = alph.index(symbol)  # символ в виде числа
            y = (a * x + b) % m
            shifr_text += alph[y]
        else:
            shifr_text += symbol  # Оставляем символы, не входящие в алфавит
    return shifr_text

def affine_deshifr(text, a, b, alph):
    deshifr_text = ""
    m = len(alph)
    a_obrat = mod_obrat(a, m)  # обратное к a по модулю
    if a_obrat is None:
        return "Ошибка: ключ 'a' и размер алфавита не взаимно простые."
    for symbol in text:
        if symbol in alph:
            y = alph.index(symbol)  # Числовое представление символа
            x = a_obrat * (y - b) % m  # Дешифрование
            deshifr_text += alph[x]
        else:
            deshifr_text += symbol  # если не входит в алфавит
    return deshifr_text

def main():
    russian_alph = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    english_alph = "abcdefghijklmnopqrstuvwxyz"

    language = input("Выбери язык (русский или английский): ").strip().lower()
    mode = input("Выбери режим (шифрование или дешифрование): ").strip().lower()
    text = input("Введи текст: ").strip().lower()
    a = int(input("Введи ключ 'a' (взаимно простое число с размером алфавита): "))
    b = int(input("Введи ключ 'b': "))

    if language in ["русский", "рус"]:
        alph = russian_alph
    elif language in ["английский", "англ"]:
        alph = english_alph
    else:
        print("Неа, попробуй другой язык.")
        return

    if mode in ["шифрование", "шифр"]:
        result = affine_shifr(text, a, b, alph)
        print("Зашифрованный текст:", result)
    elif mode in ["дешифрование", "дешифр"]:
        result = affine_deshifr(text, a, b, alph)
        print("Расшифрованный текст:", result)
    else:
        print("Ошибка, неправильный режим.")

if __name__ == "__main__":
    main()