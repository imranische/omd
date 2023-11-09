import math


class CountVectorizer:

    def __init__(self):
        self.feature_names = None

    def get_feature_names(self):
        """
        список уникальных имён создаётся при вызове метода fit_transform
        метод возвращает уже записанный список
        """
        return self.feature_names

    def fit_transform(self, corpus: list) -> list:
        """
        Строит терм-документарную матрицу и возвращает её, а также меняет
        атрибут self.feature_names, записывая в него список уникальных имён
        """
        # сначала запишем список уникальных имён в атрибут self.feature_names
        # объединяем все элементы в одну большую строку и применяем метод lower()
        s = ' '.join(corpus)
        s = s.lower()
        # записываем уникальные слова в список. Также используем множество для
        # более быстрого поиска по сравнению со списком
        word_set = set()
        feature_names = []
        for word in s.split():
            # удаляем знаки препинания
            word = word.strip('!"#$%&()*+, -./:;<=>?@[]^_`{|}~')
            if word not in word_set:
                feature_names.append(word)
                word_set.add(word)
        self.feature_names = feature_names

        # далее метод занимается записью терм-документарной матрицы
        n = len(corpus)
        list_dict = []
        count_matrix = []
        for row in corpus:
            list_dict.append(self.count_words(row))
            count_matrix.append([])
        for word in feature_names:
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
            el = el.strip('!"#$%&()*+, -./:;<=>?@[]^_`{|}~')
            count_dict[el] = count_dict.setdefault(el, 0) + 1

        return count_dict


class TfidfTransformer:

    @staticmethod
    def tf_transform(matrix):
        tf_matrix = [[] for _ in matrix]
        sums_ = [sum(it) for it in matrix]
        for i, vector in enumerate(matrix):
            tf_matrix[i] = [round(scalar / sums_[i], 3) for scalar in vector]
        return tf_matrix

    @staticmethod
    def idf_transform(count_matrix):
        count_doc = len(count_matrix)
        answer = [0 for _ in range(len(count_matrix[0]))]
        for i in range(len(count_matrix[0])):
            count_doc_with_word = 0
            for j in range(count_doc):
                if count_matrix[j][i] != 0:
                    count_doc_with_word += 1
            answer[i] = round(math.log((count_doc + 1)/(count_doc_with_word + 1)) + 1, 1)
        return answer

    def fit_transform(self, count_matrix):
        n = len(count_matrix[0])
        answer = [[0 for _ in range(n)] for _ in range(len(count_matrix))]
        for i in range(n):
            for j in range(len(count_matrix)):
                answer[j][i] = round(
                    self.tf_transform(count_matrix)[j][i] * self.idf_transform(count_matrix)[i], 3
                    )
        return answer


class TfidfVectorizer(CountVectorizer):
    def __init__(self):
        super().__init__()
        self.tfidf_ = TfidfTransformer()

    def fit_transform(self, corpus):
        count_matrix = super().fit_transform(corpus)
        return self.tfidf_.fit_transform(count_matrix)
