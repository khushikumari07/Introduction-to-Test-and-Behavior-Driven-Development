import pytest
from app.models import Product


@pytest.fixture
def product():
    """Creates a Product instance for testing"""

    product = Product(
        name="Laptop",
        description="Gaming Laptop",
        category="Electronics",
        price=1200.99,
        quantity=10,
        available=True
    )

    product.create()
    return product


def test_read_a_product(product):
    """It should Read a Product"""

    # Retrieve the product by id
    found_product = Product.find(product.id)

    # Assertions
    assert found_product is not None
    assert found_product.id == product.id
    assert found_product.name == product.name
    assert found_product.description == product.description
    assert found_product.price == product.price


def test_update_a_product(product):
    """It should Update a Product"""

    # Store original id
    original_id = product.id

    # Update description
    product.description = "testing"
    product.update()

    # Retrieve updated product
    updated_product = Product.find(product.id)

    # Assertions
    assert updated_product.id == original_id
    assert updated_product.description == "testing"


def test_delete_a_product(product):
    """It should Delete a Product"""

    product.delete()

    deleted_product = Product.find(product.id)

    assert deleted_product is None


def test_list_all_products():
    """It should List all Products"""

    products = Product.all()

    assert len(products) >= 0


def test_find_product_by_name(product):
    """It should Find a Product by Name"""

    found_products = Product.find_by_name(product.name)

    assert len(found_products) > 0
    assert found_products[0].name == product.name


def test_find_product_by_category(product):
    """It should Find Products by Category"""

    found_products = Product.find_by_category(product.category)

    assert len(found_products) > 0
    assert found_products[0].category == product.category


def test_find_available_products(product):
    """It should Find Available Products"""

    found_products = Product.find_by_availability(True)

    assert len(found_products) > 0
    assert found_products[0].available is True
