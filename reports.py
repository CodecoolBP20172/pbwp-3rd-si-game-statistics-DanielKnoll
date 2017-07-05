import reader


def count_games(file_name):
    """Returns the number of EOL characters (\n) in the file. In this data structure it is equivalent
    with the number of games. With dict the use of len() on any list gives the same result.
    """
    game_infos_string = reader.read_file(file_name, simple_string_is_enough=True)
    return game_infos_string.count("\n")


def decide(file_name, year):
    """Returns True if at least one matchins is found with the secound argument."""
    game_infos_string = reader.read_file(file_name, simple_string_is_enough=True)
    try:
        int(year)
    except ValueError as err:
        return "You should have use number: " + str(err)
    else:
        if str(year) in game_infos_string:
            return True
        else:
            return False


def get_latest(file_name):
    """Looks up the highest value from dictionayr's release dates named list and returns the
    corresponding value from dictionary's titles named list.
    """
    game_infos_dict = reader.read_file(file_name, simple_string_is_enough=False)
    latest_year = max(game_infos_dict["release dates"])
    index = game_infos_dict["release dates"].index(latest_year)
    return game_infos_dict["titles"][index]


def count_by_genre(file_name, genre):
    """Counts the matching given value in genres dictionary list"""
    game_infos_dict = reader.read_file(file_name, simple_string_is_enough=False)
    return game_infos_dict["genres"].count(genre)


def get_line_number_by_title(file_name, title):
    """Returns how many EOL characters (\n) are before the the given argument value to be found
    and raises the return value by one to get the line number.
    This solution would not cause error. But the assignment clearly instructed me to raise one.
    """
    game_infos_string = reader.read_file(file_name, simple_string_is_enough=True)
    try:
        length = game_infos_string.find(title)
        if length == -1:
            raise ValueError
    except ValueError:
        return "This title is not in the file."
    return game_infos_string[:length].count("\n") + 1


def sort_abc(file_name):
    """Return the titles dict list in order. I have used the updated bubble sort from Python SI1"""
    game_infos_dict = reader.read_file(file_name, simple_string_is_enough=False)
    return bubble_sort(game_infos_dict["titles"])


def bubble_sort(lists):
    """Had to add the lower() to the comparison for get_genres function to return the right order.
    Otherwise it would place RPG before Real-time strategy since "P" has a lower hexadecimal value
    than "a". So this function can only sort strings now.
    """
    for i in range(len(lists)-1, 0, -1):
        swapped = False
        for j in range(i):
            if lists[j].lower() > lists[j+1].lower():
                temp = lists[j]
                lists[j] = lists[j+1]
                lists[j+1] = temp
                swapped = True
        if not swapped:
            break
    return lists


def get_genres(file_name):
    """Returns sorted non redunant genres dict list through type conversions and bubble sort."""
    game_infos_dict = reader.read_file(file_name, simple_string_is_enough=False)
    try:
        sorted_non_redundant_genres_list = bubble_sort(list(set(game_infos_dict["genres"])))
    except TypeError:
        return "You changed the list to a non iterable type. Don't do that."
    else:
        return sorted_non_redundant_genres_list


def when_was_top_sold_fps(file_name):
    """Returns corresponding value from dictionayr's release dates named list with the highest selling FPS game.
    The error handling is redundant. But just in case...
    """
    game_infos_dict = reader.read_file(file_name, simple_string_is_enough=False)
    top_sell = 0.0
    game_index = 0
    for index, value in enumerate(game_infos_dict["genres"]):
        if value == "First-person shooter":
            try:
                game_sold = float(game_infos_dict["copies sold lst"][index])
            except ValueError:
                return "You did something with my primary error handling, didn't you?"
            if game_sold > top_sell:
                top_sell = game_sold
                game_index = index
    try:
        year_of_top_sold_FPS = int(game_infos_dict["release dates"][game_index])
    except ValueError:
        return "Use my primary error handling!"

    return year_of_top_sold_FPS
