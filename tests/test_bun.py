from praktikum.bun import Bun


class TestBun:

    # проверяем метод __init__, возвращается корректное значение в поле name
    def test_name_of_bun_return_correct(self):
        bun = Bun(name='Флюорисцентная булка R2-D3', price=3100.56)
        assert bun.name == 'Флюорисцентная булка R2-D3', f"Ожидается 'Флюорисцентная булка R2-D3', фактический результат - {bun.name}"

    # проверяем метод __init__, тип данных name это строка
    def test_name_of_bun_is_string(self):
        bun = Bun(name='Флюорисцентная булка R2-D3', price=3100.56)
        assert isinstance(bun.name, str), f"Ожидается str, получен {type(bun.name)}"

    # проверяем метод __init__, возвращается корректное значение в поле price
    def test_price_of_bun_return_correct(self):
        bun = Bun(name='Флюорисцентная булка R2-D3', price=3100.56)
        assert bun.price == 3100.56, f"Ожидается 3100.56, фактический результат - {bun.price}"

    # проверяем метод __init__, тип данных price это float
    def test_price_of_bun_is_float(self):
        bun = Bun(name='Флюорисцентная булка R2-D3', price=3100.56)
        assert isinstance(bun.price, float), f"Ожидается float, получен {type(bun.price)}"

    # проверяем метод get_name, корректно возвращает ожидаемое значение
    def test_get_name_returns_correct_value(self):
        bun = Bun('Краторная булка N200-i', 4567.50)
        assert bun.get_name() == 'Краторная булка N200-i', f"Ожидается 'Краторная булка N200-i', фактический результат {bun.get_name}"

    # проверяем метод get_price, корректно возвращает ожидаемое значение
    def test_get_price_returns_correct_value(self):
        bun = Bun('Краторная булка N200-i', 4567.50)
        assert bun.get_price() == 4567.50, f"Ожидается 4567.50, фактический результат - {bun.get_price}"