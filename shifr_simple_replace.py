def shifr(text, shift, alph):          #шифрование
    shifr_text = ""
    for symbol in text:
        if symbol in alph:
            index = (alph.index(symbol) + shift) % len(alph) #по модулю длины алфавита
            shifr_text += alph[index]
        else:
            shifr_text += symbol #пробел не меняем, оставляем как есть
    return shifr_text

def deshifr(text, shift, alph):         #дешифрование
    deshifr_text = ""
    for symbol in text:
        if symbol in alph:
            index = (alph.index(symbol) - shift) % len(alph) #по модулю длины алфавита
            deshifr_text += alph[index]
        else:
            deshifr_text += symbol #пробелы оствляем как есть
    return deshifr_text

def main():
    russ_alph = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    eng_alph = "abcdefghijklmnopqrstuvwxyz"

    language = input("Выбери язык (русский или английский): ").strip().lower()
    mode = input("Выбери режим (шифрование или дешифрование): ").strip().lower() #в нижний регистр и без пробелов
    text = input("Введи текст: ").strip().lower()
    shift = int(input("Введи ключ (сдвиг): "))

    if language in ["русский", "рус"]:
        alph = russ_alph
    elif language in ["английский", "англ"]:
        alph = eng_alph
    else:
        print("Неа, попробуй другой язык")
        return

    if mode in ["шифрование", "шифр"]:
        result = shifr(text, shift, alph)
        print("Зашифрованный текст:", result)
    elif mode in ["дешифрование", "дешифр"]:
        result = deshifr(text, shift, alph)
        print("Расшифрованный текст:", result)
    else:
        print("Какая-то ошибка, попробуй еще раз")

if __name__ == "__main__":
    main()