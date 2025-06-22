from unittest.mock import Mock, patch
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from conftest import burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


class TestBurger:

    # проверяем метод __init__, возвращается корректное дефолтное значение поля bun
    def test_init_default_value_bun(self, burger):
        assert burger.bun is None, f"Ожидается дефолтное значение None, фактический результат - {burger.bun}"

    # проверяем метод __init__, возвращается корректное дефолтное значение поля ingredients
    def test_init_default_value_ingredients(self, burger):
        assert burger.ingredients == [], f"Ожидается пустой список, фактический результат - {burger.ingredients}"

    # проверяем метод __init__, тип данных ingredients должен быть list
    def test_ingredients_type_is_list(self, burger):
        assert isinstance(burger.ingredients, list), f"Ожидается list, получен {type(burger.ingredients)}"

    # проверяем метод set_buns с использованием мока
    def test_set_buns_return_correct_bun(self, burger):
        mock_bun = Mock(spec=Bun)
        mock_bun.name = 'Мягкий лаваш'
        mock_bun.price = 234.80
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    # проверяем метод set_buns, что bun действительно экземпляр класса Bun
    def test_set_buns_belongs_class_bun(self, burger):
        mock_bun = Mock(spec=Bun)
        mock_bun.name = 'Мягкий лаваш'
        mock_bun.price = 234.80
        burger.set_buns(mock_bun)
        assert isinstance(burger.bun, Bun), f"Булочка не принадлежит классу Bun"

    # проверяем метод set_buns при передаче значения None
    def test_set_buns_rejects_none(self, burger):
        mock_bun = Mock(spec=Bun)
        mock_bun.name = None
        mock_bun.price = 234.80
        assert burger.bun != mock_bun, f"Название булочки не может быть None"

    # проверяем, что ingredient действительно экзмепляр класса Ingredient
    def test_ingredient_belongs_class_ingredient(self, burger):
        mock_ingredient = Mock(spec=Ingredient)
        mock_ingredient.type = INGREDIENT_TYPE_SAUCE
        mock_ingredient.name = 'кетчуп'
        mock_ingredient.price = 35.30
        burger.add_ingredient(mock_ingredient)
        assert isinstance(burger.ingredients[0], Ingredient), f"Ингредиент не принадлежит к классу Ingredient"

    # проверяем успешное добавление ингредиента с использованием мока
    def test_add_ingredient_as_mock_success(self, burger):
        mock_ingredient = Mock(spec=Ingredient)
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients[0] == mock_ingredient, f"Ингредиент не был добавлен в бургер"

    # проверяем успешное удаление ингрeдиента с использованием мока
    def test_remove_ingredient_as_mock_success(self, burger):
        mock_ingredient_1 = Mock(spec=Ingredient)
        mock_ingredient_2 = Mock(spec=Ingredient)
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        burger.remove_ingredient(0)
        assert burger.ingredients[0] == mock_ingredient_2, f"Ингредиент {burger.ingredients[0]} не был удален из бургера"

    # проверка успешного перемещения ингредиента в списке ингредиентов на другое место
    def test_move_ingredient_succes(self, burger):
        mock_ingredient_1 = Mock(spec=Ingredient)
        mock_ingredient_2 = Mock(spec=Ingredient)
        mock_ingredient_3 = Mock(spec=Ingredient)
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        burger.add_ingredient(mock_ingredient_3)
        burger.move_ingredient(2, 0)
        assert burger.ingredients == [mock_ingredient_3, mock_ingredient_1, mock_ingredient_2], f"Ингредиент {burger.ingredients[2]} не был перемещен"

    # проверяем, что метод get_price возвращает корректное значение
    @patch('praktikum.bun.Bun')
    def test_get_price_correct_result(self, mock_bun, burger):
        mock_bun.return_value.get_price.return_value = 100.20 # замокировали метод get_price класса Bun
        mock_ingredients = [Mock(get_price=Mock(return_value=20.50)),  # мок цены соуса
                            Mock(get_price=Mock(return_value=60.45))]  # мок цены начинки
        burger.set_buns(mock_bun())
        burger.ingredients = mock_ingredients
        assert burger.get_price() == 281.35, f"Ожидается 281.35, фактический результат - {burger.get_price}"

    # проверяем корректный вывод информации о бургере
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
        expected_receipt = (
    "(==== ржаная булка ====)\n"
    "= filling говяжья котлета =\n"
    "= sauce кетчуп =\n"
    "(==== ржаная булка ====)\n"
    "\n"
    "Price: 467")

        assert burger.get_receipt() == expected_receipt