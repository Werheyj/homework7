def custom_write(file_name, strings):
    strings_positions = {}
    line_number = 0
    file = open(file_name, 'w', encoding='utf-8')
    for string in strings:
        line_number += 1
        start_position = file.tell()
        file.write(string + '\n')
        strings_positions[(line_number, start_position)] = string
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test1.txt', info)
for elem in result.items():
    print(elem)
