def create_car(model, year, license_plate, / , make="not informed", engine="not informed", fuel_type="not informed"):
    print(f'Car created: {model} , {year}, {license_plate}, {make}, {engine}, {fuel_type}')

# Example usage
create_car("palio", 1999, "ABC123")  # Positional arguments for model, year, license_plate
create_car("Civic", 2020, "XYZ789", make="Honda", engine="V6", fuel_type="Diesel")  # Positional for first three, keywords for the rest
create_car("Focus", 2018, "LMN456", "Ford")  # Positional for first four, default for engine and fuel_type
create_car("Model S", 2021, "TESLA1", "Tesla", engine="Electric", fuel_type="Electric")  # All positional arguments
