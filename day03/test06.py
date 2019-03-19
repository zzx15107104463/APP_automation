import pytest


class Test01:
    @pytest.mark.parametrize('name,age,sex', [('小明', 18, '男')])
    def test01(self, name, age, sex):
        print(name)
        print(age)
        print(sex)

    def test02(self):
        print('2')


if __name__ == '__main__':
    pytest.main('-s test06.py')
