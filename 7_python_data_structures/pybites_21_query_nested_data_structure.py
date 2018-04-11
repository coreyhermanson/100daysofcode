cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def main():
    # 1. Get all Jeeps
    all_jeeps = get_all_jeeps(cars)
    print(f'String of Jeep models in order: {all_jeeps}', end='\n')

    # 2. Get the first car of every manufacturer.
    first_models = get_first_model_each_manufacturer(cars)
    print(f'List of first model of each manufacturer in order: {first_models}', end='\n')

    # 3. Get all vehicles containing the string Trail in their names (should work for other grep too)
    matching_models = get_all_matching_models(cars, grep='trail')
    print(f'List of vehicles matching search term: {matching_models}', end='\n')

    # 4. Sort the models (values) alphabetically
    sorted_models = sort_car_models(cars)
    print(f'Sorted car models dictionary: {sorted_models}', end='\n')


def get_all_jeeps(cars_dict: dict) -> str:
    """return a comma separated string of jeep models (original order)"""
    jeeps = cars_dict['Jeep']
    jeeps_string = ', '.join(jeeps)

    assert jeeps_string == 'Grand Cherokee, Cherokee, Trailhawk, Trackhawk'  # exercise test
    return jeeps_string


def get_first_model_each_manufacturer(cars_dict: dict) -> list:
    """return a list of matching models (original ordering)"""
    models_list = []
    for models in cars_dict.values():
        models_list.append(models[0])

    assert models_list == ['Falcon', 'Commodore', 'Maxima', 'Civic', 'Grand Cherokee']  # exercise test
    return models_list


def get_all_matching_models(cars_dict: dict, grep='trail') -> list:
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    models_list = []
    for model in cars_dict.values():
        for car in model:
            if grep.lower() in car.lower():
                models_list.append(car)

    models_list.sort()

    assert models_list == ['Trailblazer', 'Trailhawk']  # exercise test
    return models_list


def sort_car_models(cars_dict: dict) -> dict:
    """sort the car models (values) and return the resulting cars dict"""
    for k, v in cars_dict.items():
        sorted_values = sorted(v)
        cars_dict[k] = sorted_values

    expected = {
        'Ford': ['Fairlane', 'Falcon', 'Festiva', 'Focus'],
        'Holden': ['Barina', 'Captiva', 'Commodore', 'Trailblazer'],
        'Honda': ['Accord', 'Civic', 'Jazz', 'Odyssey'],
        'Jeep': ['Cherokee', 'Grand Cherokee', 'Trackhawk', 'Trailhawk'],
        'Nissan': ['350Z', 'Maxima', 'Navara', 'Pulsar'],
    }
    assert cars_dict == expected
    return cars_dict


if __name__ == '__main__':
    main()
