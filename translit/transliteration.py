# Переводит в транслит, заменяя пробелы знаком тире

# import modules
import click

# definition of variables
unformatted_text = str # user input
formatted_text = str

def input_text():
    """
    
    """
    user_text = input("Введите текст для транслитерации: ")
    return(user_text)


def transliterate(text):
    """
    
    """
    translit_dict = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo',
        'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm',
        'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
        'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
        'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya', ' ': '-'
    }

    def transliterate_char(char):
        return translit_dict.get(char, char)
        
    result = ''.join(transliterate_char(char) for char in text.lower())
    
    
    return result

click.clear()
formatted_text = transliterate(input_text())
print(formatted_text)
