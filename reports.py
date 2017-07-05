import reader


def count_games(file_name):
    """With this data structure I can simply make the program count the games by counting the EOL
    characters (\n) in the string since each game is in a separate line.
    It uses less memory. With dictionary I could use len() on any list for the same result.
    """
    game_infos_string = reader.read_file(file_name, simple_string_is_enough=True)
    return game_infos_string.count("\n")


def decide(file_name, year):
    """Another simple string operation, but I added a value check for the new argument."""
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
    """First question that required more complex collection. But the dictionary made the function simple.
    The program finds the highest value in the list which contains all the release dates. The title is in
    a different list ({"titles": [?,?,?,...],?,?}) but at the same index.
    I could have use a one-liner but it would have made the code harder to read.
    """
    game_infos_dict = reader.read_file(file_name, simple_string_is_enough=False)
    latest_year = max(game_infos_dict["release dates"])
    index = game_infos_dict["release dates"].index(latest_year)
    return game_infos_dict["titles"][index]


def count_by_genre(file_name, genre):
    """Here I could use a simple list count thanks to the list with the same properties inside."""
    game_infos_dict = reader.read_file(file_name, simple_string_is_enough=False)
    return game_infos_dict["genres"].count(genre)


def get_line_number_by_title(file_name, title):
    """With dictionary I could have simply use the index() method for the title and return one value higher
    to get the line number. But this can be solved with string methods also without causing error. But the
    assignment clearly instructed me to do so.
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
    """I have used the updated bubble sort from Python SI1"""
    game_infos_dict = reader.read_file(file_name, simple_string_is_enough=False)
    return bubble_sort(game_infos_dict["titles"])


def bubble_sort(lists):
    """Had to add the lower() to the comparison for get_genres to return the right order.
    So this function can only sort strings now.
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
    """I already have all the genres in list, so I convert it to set to get rid of duplicates.
    Then convert it back to list since it is the expected output. Then I sorted it with bubble
    sort. The sorted() method would place RPG before Real-time strategy since "P" has a lower
    hexadecimal value than "a".
    """
    game_infos_dict = reader.read_file(file_name, simple_string_is_enough=False)
    try:
        sorted_non_redundant_genres_list = bubble_sort(list(set(game_infos_dict["genres"])))
    except TypeError:
        return "You changed the list to a non iterable type. Don't do that."
    else:
        return sorted_non_redundant_genres_list


def when_was_top_sold_fps(file_name):
    """I could use the advantage of the same types in one list solution here too. The conversion error handling
    for this part is moved to the input file reading part. But just in case...
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
