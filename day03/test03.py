import pytest


class Test01:
    @pytest.mark.run(order=2)
    def test01(self):
        print('3')

    @pytest.mark.run(order=1)
    def test02(self):
        print('4')

if __name__ == '__main__':
    pytest.main('-s test01.py')
