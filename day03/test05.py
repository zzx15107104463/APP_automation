import pytest


@pytest.fixture(params=[1, 2, 3])
def before(request):
    return request.param


class Test01:
    def test01(self):
        print('3')

    def test02(self, before):
        print('4')
        print('before:', before)


if __name__ == '__main__':
    pytest.main('-s test01.py')
