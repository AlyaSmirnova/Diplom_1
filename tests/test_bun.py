from praktikum.bun import Bun


class TestBun:

    # проверяем метод __init__
    def test_name_of_bun_true(self):
        bun = Bun(name='Флюорисцентная булка R2-D3', price=3100.56)
        assert bun.name == 'Флюорисцентная булка R2-D3'

    def test_price_of_bun_true(self):
        bun = Bun(name='Флюорисцентная булка R2-D3', price=3100.56)
        assert bun.price == 3100.56

    # проверяем геттер get_name
    def test_get_name_returns_correct_name(self):
        bun = Bun('Краторная булка N200-i', 4567.50)
        assert bun.get_name() == 'Краторная булка N200-i'

    # проверяем геттер get_price
    def test_get_price_returns_correct_price(self):
        bun = Bun('Краторная булка N200-i', 4567.50)
        assert bun.get_price() == 4567.50
