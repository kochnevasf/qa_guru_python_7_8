"""
Протестируйте классы из модуля homework/models.py
"""
import pytest
from homework.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(product.quantity - 1)
        assert product.check_quantity(product.quantity)
        assert not product.check_quantity(product.quantity + 1), (f"Недостаточное количество {product.name} на складе. "
                                                                  f"Максмальное количество {product.quantity} шт.")

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        buying_quantity = 1
        product_quantity_before_sell = product.quantity
        remaining_quantity = product.buy(buying_quantity)
        assert remaining_quantity == product_quantity_before_sell - buying_quantity


    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        buying_quantity = product.quantity + 1
        with pytest.raises(ValueError):
            product.buy(buying_quantity)



class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """


def test_add_product(self, cart, product):
    cart.add_product(product, 1)
    assert cart.products == {product: 1}
    cart.add_product(product, 2)
    assert cart.products == {product: 3}


def test_remove_product(self, cart, product):
    cart.add_product(product, 10)
    cart.remove_product(product, 10)
    assert product not in cart.products

    cart.add_product(product, 1)
    cart.remove_product(product)
    assert product not in cart.products

    cart.add_product(product, 10)
    cart.remove_product(product, 5)
    assert cart.products == {product: 5}


def test_clear(self, cart, product):
    cart.add_product(product, 1)
    cart.clear()
    assert cart.products == {}


def test_get_total_price(self, cart, product):
    cart.add_product(product, 10)
    assert cart.get_total_price() == product.price * 10


def test_buy(self, cart, product):
    cart.add_product(product, 10)
    cart.buy()
    assert len(cart.products) == 0
    assert product.quantity == 990


def test_buy_error(self, cart, product):
    cart.add_product(product, 66666)
    with pytest.raises(ValueError):
        cart.buy()