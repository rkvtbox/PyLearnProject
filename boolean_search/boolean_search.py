# константы и переменные:
# USER_NUM_VALUES - значения введенные пользователем - длины списка, мин и макс числа для генерации
# result_list - итоговый отсортированный список заданной длины, заполненный случайными числами
# SEARCH_NUM_VALUE - значение для поиска

# Import of modules
# import time   # импорт модуля времени
import click  # импорт модуля очистки экрана консоли (win/unix)
import random # импорт модуля генерации случайных чисел
import math

from click import password_option

# Объявляем глобальные переменные
result_list_random = []
result_list_progress = []
USER_NUM_VALUES = None
SEARCH_NUM_VALUES = None


def random_num(RANDOM_NUMBER_MIN_L, RANDOM_NUMBER_MAX_L):
    """
    Функция генерации случайного числа их заданного min и max диапазона

    """
    random_int = random.randint(RANDOM_NUMBER_MIN_L, RANDOM_NUMBER_MAX_L)
    return random_int

def input_num_values():
    """
    Функция для ввода числовых значений пользователем и их проверки
    Возвращает три значения в виде библиотеки
        LEN_OF_RESULT_LIST - заданная длина списка
    для генерации случайного числа вводим границы:
        RANDOM_NUMBER_MIN - минимальное значение диапазона
        RANDOM_NUMBER_MAX - максимальное значение диапазона
        * если оба значения равны, то список заполнится одним этим числом
    """
    RNMIN = 0
    RNMAX = 0

    while True:
        LORL = input('Введите требуемое значение длины списка: ')
        if LORL.isdigit():
            break
        else:
            click.clear()  # очистка экрана от предыдущей информации
            print(f'Вы ввели неверное значение - \'{LORL}\'.\nНужно ввести целое число, попробуйте снова.')

    random_option = input('Введите \'ДА\' если хотите создать дополнительный список заполненный случайными цифрами: ')
    if random_option is True:
        while True:
            RNMIN = input('Введите минимальное число для генерации: ')
            if RNMIN.isdigit():
                break
            else:
                click.clear()  # очистка экрана от предыдущей информации
                print('Вы ввели значение длины списка:', LORL)
                print(f'Вы ввели неверное значение - \'{RNMIN}\'.\nНужно ввести целое число, попробуйте снова.')

        while True:
            RNMAX = input('Введите максимальное число для генерации: ')
            if RNMAX.isdigit() and int(RNMAX) >= int(RNMIN):
                break
            elif not RNMAX.isdigit():
                click.clear()  # очистка экрана от предыдущей информации
                print('Вы ввели значение длины списка:', LORL)
                print('Вы ввели минимальную границу для генерации: ', RNMIN)
                print(f'Введенное значение - \'{RNMAX}\' не верно.\nНужно ввести целое число, попробуйте снова.')
            elif int(RNMAX) < int(RNMIN):
                click.clear()  # очистка экрана от предыдущей информации
                print('Вы ввели значение длины списка: ', LORL)
                print('Вы ввели минимальную границу для генерации:', RNMIN)
                print(f'Введенное значение - \'{RNMAX}\' меньше указанного минимума - \'{RNMIN}\'!')
                print(f'Нужно ввести большее целое число, попробуйте снова:')



    while True:
        SRCV = input('Введите значение для поиска: ')
        if SRCV.isdigit():
           break
        else:
            print(f'Введеное значение - \'{SRCV}\' не верно.')
            print(f'Нужно ввести большее целое число, попробуйте снова:')


    return{
        'LEN_OF_RESULT_LIST': int(LORL),
        'RANDOM_NUMBER_MIN': int(RNMIN),
        'RANDOM_NUMBER_MAX': int(RNMAX),
        'SEARCH_NUM_VALUE' : int(SRCV)
    }



def list_creation(LEN_OF_RESULT_LIST):
    """
    Функция создает и сортирует два списка заданной длины (LEN_OF_RESULT_LIST):
    result_list_random - заполняет случайными числами из диапазона RANDOM_NUMBER_MIN и RANDOM_NUMBER_MAX
    result_list_progress - заполняет числами по порядку, начиная с 1

    Оба списка сортируются по возрастанию

    """
    for x in range(USER_NUM_VALUES['LEN_OF_RESULT_LIST']):
        result_list_random.append(random_num(USER_NUM_VALUES['RANDOM_NUMBER_MIN'], USER_NUM_VALUES['RANDOM_NUMBER_MAX']))

    for x in range(USER_NUM_VALUES['LEN_OF_RESULT_LIST']):
        result_list_progress.append(x+1)


    # Сортировка списков
    result_list_random.sort()

# Функция бинарного поиска, на вход подается список значений, отсортированный
def binary_search(list_for_search , target_var):
    left, right = 0, len(list_for_search) - 1 # задаем переменные левой и правой границы поиска
    count = 1 # устанавливаем счетчик количества итераций
    middle_value = int # обозначаем переменную для сравнения значения итерации

    while middle_value != target_var:
        middle_index = (left + right) // 2
        middle_value = list_for_search[middle_index]

        if middle_value == target_var:
            break
        elif middle_value < target_var:
            left = middle_index + 1
        else:
            right = middle_index - 1
        count += 1

    return {
        'VALUE' : middle_value,
        'INDEX' : middle_index,
        'COUNT' : count
    }

def result_print():
    """
    Функция выводит на экран результаты поиска в зависимости от типа введенных данных
    """
    pass




# вводим данные пользователя, определенная функция input_num_values()
USER_NUM_VALUES = input_num_values()

# создаем списки, определенные функции list_creation() и random_num()
list_creation(USER_NUM_VALUES['LEN_OF_RESULT_LIST'])
result_of_search = binary_search(result_list_progress,USER_NUM_VALUES['SEARCH_NUM_VALUE'])


# print (result_list_random)
# print (result_list_progress)
if len(result_list_progress) < 50:
    print(result_list_progress)


print('Значение поиска: ', result_of_search['VALUE'])
print('Индекс значения в списке: ', result_of_search['INDEX'])
print('Количество циклов для нахождения значения: ',result_of_search['COUNT'])
print(f'Максимально возможное количество циклов для нахождения значения - log2({USER_NUM_VALUES['LEN_OF_RESULT_LIST']}) = {math.ceil(math.log2(USER_NUM_VALUES['LEN_OF_RESULT_LIST']))}')





