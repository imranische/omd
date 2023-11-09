from hometask_4 import CountVectorizer, TfidfTransformer, TfidfVectorizer

if __name__ == '__main__':
    corpus = [
     'Crock, !Pot Pasta Never? boil! pasta again',
     'Pasta Pomodoro .Fresh !ingredients Parmesan to taste'
    ]

    # CountVectorizer (задание 1)
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(f'смотрим работу count_vectorizer, на вход подаём: \
    \n{corpus}')
    print(f'feature_names = {vectorizer.get_feature_names()}')
    print('count_matrix:')
    print(count_matrix)

    # term frequency (задание 2)
    print()
    print('выполняем tf-transform, на вход подаём полученную count_matrix')
    transformer_0 = TfidfTransformer()
    tf_matrix = transformer_0.tf_transform(count_matrix)
    print('tf_matrix:')
    print(tf_matrix)

    # inverse document-frequency (задание 3)
    print()
    print('выполняем idf-transform, на вход подаём  count_matrix')
    idf_matrix = transformer_0.idf_transform(count_matrix)
    print('idf_matrix:')
    print(idf_matrix)

    # tf-idf transformer (задание 4)
    print()
    print('выполняем tf-idf transform, на вход подаём  count_matrix')
    transformer = TfidfTransformer()
    tfidf_matrix = transformer.fit_transform(count_matrix)
    print('idf_matrix:')
    print(tfidf_matrix)

    # tf-idf vectorizer (задание 5)
    print()
    print('сейчас посмотрим работу метода fit_transform класса TfidfVectorizer')
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    tf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tf_vectorizer.fit_transform(corpus)
    print(tf_vectorizer.get_feature_names())
    print(tfidf_matrix)
