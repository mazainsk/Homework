# Домашнее задание по теме "Оператор "with"
import re

class WordsFinder:
    _CHRS = "[,.=!?:;]|' - '"       # Регулярное выражение для поиска и удаления
                # P.S.: Как альтернатива есть еще функция translate в связке со строковым методом maketrans

    def __init__(self, *file_names):
        self.file_names = (name for name in file_names)

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r',  encoding='utf-8') as file:
                words = []
                for line in file:
                    line = line.lower()
                    line = re.sub(self._CHRS, '', line)
                    words += line.split()
                all_words[file_name] = words
        return all_words

    def find(self, word: str):
        finds = {}
        word = word.lower()
        all_words = self.get_all_words()
        for k, v in all_words.items():
            finds[k] = v.index(word) + 1    # нужен номер слова (от 1), а не его индекс (от 0)
        return finds

    def count(self, word: str):
        finds = {}
        word = word.lower()
        for k, v in self.get_all_words().items():
            finds[k] = v.count(word)
        return finds

# Проверка на тестовых данных
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))