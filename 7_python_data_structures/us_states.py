from states_data import us_state_abbrev
from states_data import states_list


def main(state_list, state_dict):
    ordered = sorted(state_dict.items())

    # Print out the 10th item in each
    list_10 = state_list[9]
    dict_10 = ordered[9]

    print(f'10th item in LIST: {list_10}')
    print(f'10th item in DICT: {dict_10}')

    # Print out the 45th key in the dictionary
    dict_45_key = ordered[44][0]

    print(f'45th key in DICT: {dict_45_key}')

    # Print out the 27th value in the dictionary
    dict_27_value = ordered[26][1]

    print(f'27th value in DICT: {dict_27_value}')

    # Replace the 15th key in the dictionary with the 28th item in the list.
    dict_15_key = ordered[14][0]
    list_28_item = states_list[27]

    print(f'Replacing the DICT key {dict_15_key} with the the 28th item in the list: {list_28_item}')

    state_dict[list_28_item] = state_dict.pop(dict_15_key)
    print(f'After replacing, the DICT key {list_28_item} results in a value of {state_dict[list_28_item]}')


if __name__ == '__main__':
    main(states_list, us_state_abbrev)
