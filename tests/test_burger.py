from unittest.mock import Mock, patch
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from conftest import burger


class TestBurger:

    # проверяем метод __init__
    def test_init_default_values(self, burger):
        assert burger.bun is None
        assert burger.ingredients == []

    # проверяем метод set_buns с использованием мока
    def test_set_buns_with_correct_bun(self, burger):
        mock_bun = Mock(spec=Bun)
        mock_bun.name = 'Мягкий лаваш'
        mock_bun.price = 234.80
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    # проверяем успешное добавление ингредиента с использованием мока
    def test_add_ingredient_as_mock_success(self, burger):
        mock_ingredient = Mock(spec=Ingredient)
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients[0] == mock_ingredient

    # проверка успешного удаления ингридиента с использованием мока
    def test_remove_ingridient_as_mock_success(self, burger):
        mock_ingredient_1 = Mock(spec=Ingredient)
        mock_ingredient_2 = Mock(spec=Ingredient)
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        burger.remove_ingredient(0)
        assert burger.ingredients[0] == mock_ingredient_2

    # проверка успешного перемещения ингридента в списке ингридиентов на другое место
    def test_move_ingredient_succes(self, burger):
        mock_ingredient_1 = Mock(spec=Ingredient)
        mock_ingredient_2 = Mock(spec=Ingredient)
        mock_ingredient_3 = Mock(spec=Ingredient)
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        burger.add_ingredient(mock_ingredient_3)
        burger.move_ingredient(2, 0)
        assert burger.ingredients == [mock_ingredient_3, mock_ingredient_1, mock_ingredient_2]

    #
    @patch('praktikum.bun.Bun')
    def test_get_price_correct_result(self, mock_bun, burger):
        mock_bun.return_value.get_price.return_value = 100.20  # замокировали метод get_price у класса Bun
        mock_ingredients = [Mock(get_price=Mock(return_value=20.50)),  # мок цены соуса
                            Mock(get_price=Mock(return_value=60.45))]  # мок цены начинки
        burger.set_buns(mock_bun())
        burger.ingredients = mock_ingredients

        assert burger.get_price() == 281.35

    @patch('praktikum.burger.Burger.get_price')  # замокировали метод get_price у бургера
    def test_get_receipt(self, mock_get_price, burger):
        mock_bun = Mock()
        mock_bun.get_name.return_value = 'ржаная булка'
        burger.bun = mock_bun

        mock_ingredient_1 = Mock()
        mock_ingredient_1.get_name.return_value = 'говяжья котлета'
        mock_ingredient_1.get_type.return_value = 'FILLING'

        mock_ingredient_2 = Mock()
        mock_ingredient_2.get_name.return_value = 'кетчуп'
        mock_ingredient_2.get_type.return_value = 'SAUCE'

        burger.ingredients = [mock_ingredient_1, mock_ingredient_2]
        mock_get_price.return_value = 467

        expected_receipt = '''(=== ржаная булка ===)
        = filling говяжья котлета =
        = sauce кетчуп =
        (=== ржаная булка ===)

        Price: 467'''

        assert burger.get_receipt() == expected_receipt
