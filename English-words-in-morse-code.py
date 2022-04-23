from random import choice


def morse_encode(word, morse_symbols):
    """Return translates a word in English into a sequence of dots and dashes.

    Keyword arguments:
    word -- list words in English
    morse_symbols -- morse code dictionary.

    """
    word_in_morse_code = ''
    for symbol in word:
        word_in_morse_code += morse_symbols[symbol] + ' '
    return word_in_morse_code


def get_word(words):
    """Return randomly selected word.

    Keyword arguments:
    word -- list words in English.

    """
    return choice(words)


def print_statistics(answers):
    """Return list with number of answers.

    Keyword arguments:
    answers -- list of correct and incorrect answers.

    """
    counter_all = len(answers)
    counter_correct = answers.count(True)
    counter_incorrect = answers.count(False)
    return [counter_all, counter_correct, counter_incorrect]


morse_symbols = {
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
    "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.",
    "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..",
    "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.",
    "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
    "y": "-.--", "z": "--..", ".": ".-.-.-", ",": "--..--", "?": "..--..",
    "!": "-.-.--", "-": "-....-", "/": "-..-.", "@": ".--.-.", "(": "-.--.",
    ")": "-.--.-"
}
list_english_words = ['code', 'bit', 'list', 'soul', 'next']
answers = []
counter = 0
stop = ''

start = input('''Сегодня мы потренируемся расшифровывать морзянку.
Нажмите Enter и начнем ''')
while True:
    if stop.lower() != 'выход':
        counter += 1

        word = get_word(list_english_words)
        word_in_morse_code = morse_encode(word, morse_symbols)
        print('Слово {} >>> {}'.format(counter, word_in_morse_code))

        answer = input('Расшифруйте и введите ответ: ').lower()
        if answer == word:
            answers.append(answer == word)
            print(f'Верно, {word.title()}!')
        else:
            answers.append(answer == word)
            print(f'Не верно, правильный ответ {word.title()}!')
        stop = input('Нажмите Enter чтобы продолжить или введите Выход для завершения ')
    else:
        print(f'Всего задачек: {print_statistics(answers)[0]}')
        print(f'Отвечено верно: {print_statistics(answers)[1]}')
        print(f'Отвечено неверно: {print_statistics(answers)[2]}')
        break
