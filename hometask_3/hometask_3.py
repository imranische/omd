class CountVectorizer:

    @staticmethod
    def get_feature_names(corpus: list) -> list:
        """
        Создаёт список уникальных слов из списка строк
        и возвращает его
        """
        # объединяем все элементы в одну большую строку и применяем метод lower()
        s = ' '.join(corpus)
        s = s.lower()
        # записываем уникальные слова в список. Также используем множество для
        # более быстрого поиска по сравнению со списком
        word_set = set()
        word_list = []
        for word in s.split():
            # удаляем знаки препинания
            word = word.strip('!"#$%&()*+, -./:;<=>?@[\]^_`{|}~')
            if word not in word_set:
                word_list.append(word)
                word_set.add(word)
        return word_list

    def fit_transform(self, corpus: list) -> list:
        """
        Строит терм-документарную матрицу и возвращает её
        """
        n = len(corpus)
        feauture_list = self.get_feature_names(corpus)
        list_dict = []
        count_matrix = []
        for row in corpus:
            list_dict.append(self.count_words(row))
            count_matrix.append([])
        for word in feauture_list:
            for i in range(n):
                count_matrix[i].append(list_dict[i].get(word, 0))

        return count_matrix

    @staticmethod
    def count_words(s: str) -> dict:
        """
        Возвращает словарь, ключи которого - уникальные слова, встречающиеся в
        строке s, значения - количество слов в этой строке
        """
        s = s.lower()
        word_list = s.split()
        count_dict = {}
        for el in word_list:
            el = el.strip('!"#$%&()*+, -./:;<=>?@[\]^_`{|}~')
            count_dict[el] = count_dict.setdefault(el, 0) + 1

        return count_dict
