def fuel_cost(distance_km: float, mileage_kmpl: float, fuel_price_per_litre: float) -> float:
    """
    Calculate the total fuel cost for a trip.

    :param distance_km: total distance to travel, in kilometers
    :param mileage_kmpl: vehicle's fuel efficiency, in km per litre
    :param fuel_price_per_litre: current fuel price per litre
    :return: total fuel cost, rounded to 2 decimal places
    """
    if distance_km < 0 or mileage_kmpl <= 0 or fuel_price_per_litre < 0:
        raise ValueError("distance and price must be non-negative, and mileage must be greater than 0")

    litres_needed = distance_km / mileage_kmpl
    total_cost = litres_needed * fuel_price_per_litre
    return round(total_cost, 2)
