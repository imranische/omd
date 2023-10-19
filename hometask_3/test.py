from hometask_3 import CountVectorizer

if __name__ == '__main__':
    corpus = [
     'Crock, !Pot Pasta Never? boil! pasta again',
     'Pasta Pomodoro .Fresh !ingredients Parmesan to taste'
    ]

    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names(corpus))
    print(count_matrix)
