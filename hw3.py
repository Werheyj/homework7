import string


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = tuple(file_names)

    def get_all_words(self):
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                content = file.read()
                content = content.lower()
                for p in string.punctuation:
                    if p in content:
                        content = content.replace(p, '')
                list_ = content.split()
                all_words = {file_name: list_}
        return all_words

    def find(self, word):
        result_find = {}
        for name, words in self.get_all_words().items():
            first_position = words.index(word.lower()) + 1
            result_find = {name: first_position}
        return result_find

    def count(self, word):
        result_count = {}
        for name, words in self.get_all_words().items():
            counter = 0
            for w in words:
                if w == word.lower():
                    counter += 1
            result_count = {name: counter}
        return result_count


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))   # 4 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
