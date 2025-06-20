# Домашнее задание по теме "Позиционирование в файле"

def custom_write(file_name: str, strings: list[str]):
    strings_positions = {}
    with open(file_name, 'w', encoding='utf-8') as  file:
        for i, string in enumerate(strings, 1):
            string_begining = file.tell()
            file.write(string + '\n')
            # strings_positions.update({(i, string_begining): string})  # очень избыточно!! см.ниже
            strings_positions[(i, string_begining)] = string    # при обращении по отсутствующему ключу в словарь
            # автоматически добавится этот новый ключ и мы сразу присвоим ключу значение
    return strings_positions

# Тестовые данные для проверки

info = ['Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!']

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)