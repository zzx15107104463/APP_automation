import pytest


class Test01:
    def setup(self):
        print('1')

    def teardown(self):
        print('2')

    def test01(self):
        print('3')

    def test02(self):
        print('4')

if __name__ == '__main__':
    pytest.main('-s test01.py')
