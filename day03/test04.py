import pytest


@pytest.fixture(scope='class', autouse=True)
def before():
    print('1')


class Test01:
    def test01(self):
        print('3')

    def test02(self):
        print('4')


if __name__ == '__main__':
    pytest.main('-s test01.py')
