import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cost_estimator.fuel import fuel_cost


def test_fuel_cost_basic():
    # 100 km, mileage 20 km/l, price ₹100/litre -> 5 litres * 100 = 500
    assert fuel_cost(100, 20, 100) == 500.0


def test_fuel_cost_rounding():
    # 150 km, mileage 17 km/l, price ₹95/litre -> should round to 2 decimals
    result = fuel_cost(150, 17, 95)
    assert result == round((150 / 17) * 95, 2)


def test_fuel_cost_zero_distance():
    # zero distance should cost zero, not error
    assert fuel_cost(0, 20, 100) == 0.0


def test_fuel_cost_negative_distance_raises():
    with pytest.raises(ValueError):
        fuel_cost(-10, 20, 100)


def test_fuel_cost_zero_mileage_raises():
    with pytest.raises(ValueError):
        fuel_cost(100, 0, 100)
