import pytest
from datetime import datetime, timedelta
from price_tracker import parse_data, get_price_change

@pytest.fixture
def sample_data():
    return [
        {'name': 'Товар A', 'date': datetime(2023, 10, 1), 'price': 100.0},
        {'name': 'Товар A', 'date': datetime(2023, 10, 15), 'price': 110.0},
        {'name': 'Товар B', 'date': datetime(2023, 10, 5), 'price': 50.0},
    ]

def test_parse_data():
    with open('test_data.txt', 'w') as f:
        f.write('Товар A,2023-10-01,100.0\nТовар B,2023-10-05,50.0')

    data = parse_data('test_data.txt')
    assert len(data) == 2
    assert data[0]['name'] == 'Товар A'
    assert data[0]['price'] == 100.0

@pytest.mark.parametrize("product_name, expected_change", [
    ('Товар A', 10.0),
    ('Товар B', 0.0),
    ('Товар C', None),
])
def test_get_price_change(sample_data, product_name, expected_change):
    assert get_price_change(sample_data, product_name) == expected_change
