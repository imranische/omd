from morse import decode

def test_1():
    assert decode('.--. -.-- - .... --- -.') == 'PYTHON'

def test_2():
    assert decode('... --- ...') == 'SOS1'

def test_3():
    assert decode('..   .-- .- -. -   - ---   ... .-.. . . .--.') == 'IWANTTOSLEEP_bla_bla_bla'

if __name__ == '__main__':
    test_1()
    test_2()
    test_3()

