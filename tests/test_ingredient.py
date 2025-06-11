from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


class TestIngredient:

    def test_create_ingredient_is_successfil(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Сырный соус', 10.25)
        assert (
                ingredient.type,
                ingredient.name,
                ingredient.price
               ) == (
                INGREDIENT_TYPE_SAUCE,
                'Сырный соус',
                10.25)

    def test_get_price_return_correct_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Чили соус', 12.25)
        assert ingredient.get_price() == 12.25

    def test_get_name_return_correct_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Чили соус', 12.25)
        assert ingredient.get_name() == 'Чили соус'

    def test_get_type_return_correct_type(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Чили соус', 12.25)
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE
