from one_hot_encoder import fit_transform


def test_1():
    actual = fit_transform(['Moscow', 'New York', 'Moscow', 'London'])
    exp_transformed = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
        ]
    assert actual == exp_transformed


def test_2():
    actual = fit_transform(['crock', 'pot', 'pasta', 'never', 'boil', 'pasta', 'again'])
    exp_transformed = [
        ('crock', [0, 0, 0, 0, 0, 1]),
        ('pot', [0, 0, 0, 0, 1, 0]),
        ('pasta', [0, 0, 0, 1, 0, 0]),
        ('never', [0, 0, 1, 0, 0, 0]),
        ('boil', [0, 1, 0, 0, 0, 0]),
        ('pasta', [0, 0, 0, 1, 0, 0]),
        ('again', [1, 0, 0, 0, 0, 0])
        ]
    assert actual == exp_transformed


def test_3():
    actual = fit_transform(['pasta', 'pomodoro', 'fresh', 'ingredients', 'parmesan', 'to', 'taste'])
    exp_transformed = [
        ('pasta', [0, 0, 0, 0, 0, 0, 1]),
        ('pomodoro', [0, 0, 0, 0, 0, 1, 0]),
        ('fresh', [0, 0, 0, 0, 1, 0, 0]),
        ('ingredients', [0, 0, 0, 1, 0, 0, 0]),
        ('parmesan', [0, 0, 1, 0, 0, 0, 0]),
        ('to', [0, 1, 0, 0, 0, 0, 0]),
        ('taste', [1, 0, 0, 0, 0, 0, 0])
        ]
    assert actual == exp_transformed


def test_4():
    actual = fit_transform(['vodka', 'vodka', 'boris', 'eltsin'])
    exp_transformed = [
        ('vodka', [0, 0, 1]),
        ('vodka', [0, 0, 1]),
        ('boris', [0, 1, 0]),
        ('eltsin', [1, 0, 0])
        ]
    assert actual == exp_transformed
