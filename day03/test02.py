import pytest


class Test01:
    def setup_class(self):
        print('01')

    def teardown_class(self):
        print('02')

    def setup(self):
        print('1')

    def teardown(self):
        print('2')

    def test01(self):
        print('3')

    def test02(self):
        print('4')

if __name__ == '__main__':
    pytest.main('-s test02.py')
