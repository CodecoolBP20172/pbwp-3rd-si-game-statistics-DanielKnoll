import reader


def get_most_played(file_name):
    """Looks up the highest value from dictionayr's copies sold lst named list and returns the
    corresponding value from dictionary's titles named list.
    """
    game_infos_dict = reader.read_file(file_name, simple_string_is_enough=False)
    temp = game_infos_dict["copies sold lst"]
    most_sold = [float(temp[i]) for i in range(len(temp))]
    index = most_sold.index(max(most_sold))
    return game_infos_dict["titles"][index]


def sum_sold(file_name):
    """Returns the sum of dictionayr's copies sold lst named list"""
    game_infos_dict = reader.read_file(file_name, simple_string_is_enough=False)
    temp = game_infos_dict["copies sold lst"]
    return sum([float(temp[i]) for i in range(len(temp))])


def get_selling_avg(file_name):
    """Returns the sum of dictionayr's copies sold lst named list"""
    game_infos_dict = reader.read_file(file_name, simple_string_is_enough=False)
    temp = game_infos_dict["copies sold lst"]
    sold_float_list = [float(temp[i]) for i in range(len(temp))]
    return sum(sold_float_list) / len(sold_float_list)

