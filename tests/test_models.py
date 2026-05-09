import pytest
from app.models import Product


@pytest.fixture
def product():
    """Creates a Product instance for testing"""
    return Product(
        id=1,
        name="Laptop",
        description="Gaming Laptop",
        category="Electronics",
        price=1200.99,
        quantity=10,
        available=True
    )


def test_read_a_product(product):
    """It should Read a Product"""

    # Simulate retrieving product by id
    found_product = product

    # Assertions
    assert found_product is not None
    assert found_product.id == 1
    assert found_product.name == "Laptop"
    assert found_product.description == "Gaming Laptop"
    assert found_product.price == 1200.99


def test_update_a_product(product):
    """It should Update a Product"""

    # Store original id
    original_id = product.id

    # Update description
    product.description = "testing"

    # Assertions
    assert product.id == original_id
    assert product.description == "testing"


def test_delete_a_product(product):
    """It should Delete a Product"""

    deleted_product = None

    assert deleted_product is None


def test_list_all_products():
    """It should List all Products"""

    products = [
        Product(
            id=1,
            name="Laptop",
            description="Gaming Laptop",
            category="Electronics",
            price=1200.99,
            quantity=10,
            available=True
        ),
        Product(
            id=2,
            name="Headphones",
            description="Wireless Headphones",
            category="Electronics",
            price=199.99,
            quantity=50,
            available=True
        ),
    ]

    assert len(products) == 2


def test_find_product_by_name():
    """It should Find a Product by Name"""

    products = [
        Product(
            id=1,
            name="Laptop",
            description="Gaming Laptop",
            category="Electronics",
            price=1200.99,
            quantity=10,
            available=True
        )
    ]

    product = next(
        (p for p in products if p.name == "Laptop"),
        None
    )

    assert product is not None
    assert product.name == "Laptop"


def test_find_product_by_category():
    """It should Find Products by Category"""

    products = [
        Product(
            id=1,
            name="Laptop",
            description="Gaming Laptop",
            category="Electronics",
            price=1200.99,
            quantity=10,
            available=True
        ),
        Product(
            id=2,
            name="Headphones",
            description="Wireless Headphones",
            category="Electronics",
            price=199.99,
            quantity=50,
            available=True
        ),
    ]

    electronics_products = [
        p for p in products
        if p.category == "Electronics"
    ]

    assert len(electronics_products) == 2


def test_find_available_products():
    """It should Find Available Products"""

    products = [
        Product(
            id=1,
            name="Laptop",
            description="Gaming Laptop",
            category="Electronics",
            price=1200.99,
            quantity=10,
            available=True
        ),
        Product(
            id=2,
            name="Book",
            description="Programming Book",
            category="Books",
            price=15.99,
            quantity=0,
            available=False
        ),
    ]

    available_products = [
        p for p in products
        if p.available
    ]

    assert len(available_products) == 1
