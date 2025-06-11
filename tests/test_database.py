import pytest
from praktikum.database import Database
from conftest import database
from conftest import expected_ingredients


class TestDatabase:

    def test_available_buns_returns_list(self, database):
        buns = database.available_buns()
        assert isinstance(buns, list)

    def test_len_list_buns_is_three(self, database):
        buns = database.available_buns()
        assert len(buns) == 3

    @pytest.mark.parametrize('index', [0, 1, 2])
    def test_available_buns_content(self, database, index):
        bun = database.available_buns()[index]
        expected_bun = Database().available_buns()[index]
        assert (bun.name, bun.price) == (expected_bun.name, expected_bun.price)

    @pytest.mark.parametrize('index', list(range(6)))
    def test_available_ingredients_content(self, database, expected_ingredients, index):
        ingredient = database.available_ingredients()[index]
        expected_content = expected_ingredients[index]
        assert (ingredient.type, ingredient.name, ingredient.price) == expected_content