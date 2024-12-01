# Напишите функцию, которая принимает строку и возвращает её в верхнем регистре.
# Напишите функцию, которая принимает строку и возвращает её в нижнем регистре.
# Напишите функцию, которая принимает строку и возвращает её с заглавной первой буквой.
# Напишите функцию, которая принимает строку и возвращает её с заглавной первой буквой каждого слова.
# Напишите функцию, которая принимает строку и возвращает её, заменив все пробелы на подчеркивания.
# Напишите функцию, которая принимает строку и возвращает её, удалив все пробелы.
# Напишите функцию, которая принимает строку и возвращает её, заменив все вхождения одного символа на другой символ.
# Напишите функцию, которая принимает строку и возвращает её, разделив её на слова и вернув список слов.
# Напишите функцию, которая принимает строку и возвращает её, удалив все знаки препинания.
# Напишите функцию, которая принимает строку и возвращает её, заменив все цифры на символ '#'.

text_input = "Привет Питон, как  дела? 12345 Все хорошо? 1254"
char_to_find = 'т'
char_to_replace = 'X'
chars_to_replace = []


def string_to_upper(text):
    return (text.upper())

def string_to_lower(text):
    return (text.lower())

def string_first_upper(text):
    return (text[0].upper() + text[1:].lower())

def string_everyfirst_upper (text):
    result = ''
    for index in range (len(text)):
        if text[index-1] == ' ' or index == 0:
            result += text[index].upper()
        else:
            result += text[index].lower()
            
    return (result)

def string_change_to_underscore(text):
    result = ''
    for index in range (len(text)):
        if text[index] == ' ':
            result += '_'
        else:
            result += text[index]
    return (result)

def string_del_spaces(text):
    result = ''
    for index in range (len(text)):
        if text[index] == ' ':
            result += ''
        else:
            result += text[index]
    return (result)

def string_change_char (text, char_to_find, char_to_replace):
    result = ''
    for index in range (len (text)):
        if text[index] == char_to_find:
            result += char_to_replace
        else:
             result += text[index]   
    return (result)

def string_to_list(text):
    return (text.split())

def string_del_punctuation_marks (text):
    punctuation_marks = (
        '.', ',', '?'
    )
    result = ''
    for index in range (len (text)):
        if text[index] in punctuation_marks:
            result += ''
        else:
            result += text[index]
    return (result)        
    
def string_change_numbers(text):
    result = ''
    num_list = (
        '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'
    )
    for index in range (len (text)):
        if text[index] in num_list:
            result += '#'
        else:
            result += text[index]
    return (result)

    
print (f'Изначальный текст: {text_input}')
print()
print (f'1 (все заглавные): {string_to_upper(text_input)}')
print (f'2 (все прописные): {string_to_lower(text_input)}')
print (f'3 (первая буква заглавная): {string_first_upper(text_input)}')
print (f'4 (каждое слово с заглавной): {string_everyfirst_upper(text_input)}')
print (f'5 (замена пробелов подчеркиванием): {string_change_to_underscore(string_everyfirst_upper(text_input))}')
print (f'6 (удаление всех пробелов) {string_del_spaces(text_input)}')
print (f'7 (замена символа): {string_change_char(text_input, char_to_find, char_to_replace)}')
print (f'8 (строка в список): {string_to_list(text_input)}')
print  (f'9 (удаление знаков препинания) {string_del_punctuation_marks(text_input)}')

print (f'10 (замена цифр на #): {string_change_numbers(text_input)}')