import reader


def get_most_played(file_name):
    """Looks up the highest value from dictionayr's copies sold lst named list and returns the
    corresponding value from dictionary's titles named list.
    """
    preferences_dict = reader.read_file(file_name, simple_string_is_enough=False)
    sold_float = list(map(lambda x: float(x), preferences_dict["copies sold lst"]))
    index = sold_float.index(max(sold_float))
    return preferences_dict["titles"][index]


def sum_sold(file_name):
    """Returns the summary of dictionayr's copies sold lst named list"""
    preferences_dict = reader.read_file(file_name, simple_string_is_enough=False)
    return sum(map(lambda x: float(x), preferences_dict["copies sold lst"]))


def get_selling_avg(file_name):
    """Returns the average of dictionayr's copies sold lst named list"""
    preferences_dict = reader.read_file(file_name, simple_string_is_enough=False)
    sold_float_list = list(map(lambda x: float(x), preferences_dict["copies sold lst"]))
    return sum(sold_float_list) / len(sold_float_list)


def count_longest_title(file_name):
    """Returns the length of dictionayr's titles named list's longest title"""
    preferences_dict = reader.read_file(file_name, simple_string_is_enough=False)
    return max(map(lambda x: len(x), preferences_dict["titles"]))


def get_date_avg(file_name):
    """Returns the average of dictionayr's release dates named list"""
    preferences_dict = reader.read_file(file_name, simple_string_is_enough=False)
    dates_float_list = list(map(lambda x: int(x), preferences_dict["release dates"]))
    date_avg = sum(dates_float_list) / len(dates_float_list)
    return round(date_avg)


def get_game(file_name, title):
    """Returns each properties of the given title in a list"""
    preferences_str = reader.read_file(file_name, simple_string_is_enough=True)
    pref_lst = preferences_str.splitlines()
    for i, line in enumerate(pref_lst):
        if title in line:
            if title == (line.split("\t"))[0]:
                break
    if i+1 == len(pref_lst) and title not in line:
        return "No such game."
    title_properties = line.split("\t")
    try:
        title_properties[1] = float(title_properties[1])
        title_properties[2] = int(title_properties[2])
    except ValueError:
        return "check_errors_in_file or check_conversion_error function(s) are removed"\
               "or missing func call in reader.py"
    return title_properties


def count_grouped_by_genre(file_name):
    preferences_dict = reader.read_file(file_name, simple_string_is_enough=False)
    try:
        genres_lst = list(set(preferences_dict["genres"]))
    except TypeError:
        return "You messed up the dict with your code. GJ"

    genre_count_dict = {}
    for genre_key in genres_lst:
        count_value = preferences_dict["genres"].count(genre_key)
        genre_count_dict[genre_key] = count_value
    return genre_count_dict
