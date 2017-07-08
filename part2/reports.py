import reader


def get_most_played(file_name):
    """Looks up the highest value from dictionary's copies sold lst named list and returns the
    corresponding value from dictionary's titles named list.
    """
    preferences_dict = reader.read_file(file_name, simple_string_is_enough=False)
    index = preferences_dict["copies sold lst"].index(max(preferences_dict["copies sold lst"]))
    return preferences_dict["titles"][index]


def sum_sold(file_name):
    """Returns the summary of dictionary's copies sold lst named list"""
    preferences_dict = reader.read_file(file_name, simple_string_is_enough=False)
    return sum(preferences_dict["copies sold lst"])


def get_selling_avg(file_name):
    """Returns the average of dictionary's copies sold lst named list"""
    preferences_dict = reader.read_file(file_name, simple_string_is_enough=False)
    return sum(preferences_dict["copies sold lst"]) / len(preferences_dict["copies sold lst"])


def count_longest_title(file_name):
    """Returns the length of dictionary's titles named list's longest title"""
    preferences_dict = reader.read_file(file_name, simple_string_is_enough=False)
    return max(map(lambda x: len(x), preferences_dict["titles"]))


def get_date_avg(file_name):
    """Returns the average of dictionary's release dates named list"""
    preferences_dict = reader.read_file(file_name, simple_string_is_enough=False)
    date_avg = sum(preferences_dict["release dates"]) / len(preferences_dict["release dates"])
    return round(date_avg)


def get_game(file_name, title):
    """Returns each properties of the given title in a list"""
    preferences_dict = reader.read_file(file_name, simple_string_is_enough=False)
    try:
        index = preferences_dict["titles"].index(title)
    except ValueError:
        return "No such game in the file."
    preferences = ["titles", "copies sold lst", "release dates", "genres", "publishers"]
    title_properties = [preferences_dict[key][index] for key in preferences]
    return title_properties


def count_grouped_by_genre(file_name):
    """Returns a dictionary with genre names as keys and with the total number of that genre."""
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


def get_date_ordered(file_name):
    """This ugly code returns a double sorted title list ordered by release dates.
    It searches matches in the sorted dates and sorts those slices in titles."""
    preferences_dict = reader.read_file(file_name, simple_string_is_enough=False)

    year = preferences_dict["release dates"]
    indexes = [x for x in range(len(year))]
    indexes.sort(key=year.__getitem__, reverse=True)
    title = [preferences_dict["titles"][x] for x in indexes]

    match = {}
    year = sorted(preferences_dict["release dates"], reverse=True)
    i = 0
    while i < len(year)-1:
        if year[i] == year[i+1]:
            match[i] = 2
            j = i + 1
            while year[j] == year[j+1]:
                match[i] += 1
                j += 1
            i += match[i]
        i += 1
    for key in match:
        swap = title[key:key+match[key]]
        swap.sort(key=str.lower)
        title[key:key+match[key]] = swap

    return title
