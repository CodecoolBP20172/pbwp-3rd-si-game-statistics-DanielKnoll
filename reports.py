

def read_file(file_name, simple_string_is_enough):
    """In the first version the file reading used with open, but I found out that some functions
    can return the correct value from a simple string. So I made two separate readers. One returns
    a string the other returns a dictionary. In order to do that I had to keep open the file
    until the return command. At least in this case there is only one line in the try.
    """
    try:
        file = open(file_name)
    except FileNotFoundError:
        return "The game_stat.txt file is missing, or incorrect filename given."
    else:
        error = check_errors_in_file(file, file_name)
        if error != "No errors":
            exit(error)

        if simple_string_is_enough:
            game_infos = convert_file_to_string(file)
        else:
            game_infos = convert_file_to_dict(file)
        file.close()
        return game_infos


def check_errors_in_file(file, file_name):
    """Next task"""
    for line_num, line in enumerate(file):
        if line.count("\t") != 4:
            return "InputError: You have incorrect number of values in line " \
                   + str(line_num) + " in " + file_name \
                   + "\nExpected values: title->total copies sold->release date->genre->publisher↲"
    file.seek(0)
    return "No errors"


def convert_file_to_string(file):
    """For the first two questions for example f I can simply return a string to work with."""
    game_infos_string = file.read()
    return game_infos_string


def convert_file_to_dict(file):
    """For the most of the questions the program will create a dictionary for each function call.
    Instead of doing the obvious and storing the file line by line in lists I figured I can use
    simple commands if I store the columns in separate lists. I used the property names as keys
    so it will be easier to read the code.
    Since the information categories are in the same order as in the file I could append the right
    value to the right dictionary key. The game informations will bein the same indexes but in
    different lists.
    I got rid of the '\n' with a slice command at the end of each line, and split the line at tabulators.
    """
    game_infos_dict = {}
    info_categories = ["titles", "copies sold lst", "release dates", "genres", "publishers"]
    for key in info_categories:
        game_infos_dict.update({key: []})

    for line in file:
        one_game = line[:-1].split("\t")
        for index, value in enumerate(one_game):
            game_infos_dict[info_categories[index]].append(value)

    return game_infos_dict


def count_games(file_name):
    """With this data structure I can simply make the program count the games by counting the EOL
    characters (\n) in the string since each game is in a separate line.
    It uses less memory. With dictionary I could use len() on any list for the same result.
    """
    game_infos_string = read_file(file_name, simple_string_is_enough=True)
    return game_infos_string.count("\n")


def decide(file_name, year):
    """Another simple string operation, but I added a value check for the new argument."""
    game_infos_string = read_file(file_name, simple_string_is_enough=True)
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
    game_infos_dict = read_file(file_name, simple_string_is_enough=False)
    latest_year = max(game_infos_dict["release dates"])
    index = game_infos_dict["release dates"].index(latest_year)
    return game_infos_dict["titles"][index]


def count_by_genre(file_name, genre):
    """Here I could use a simple list count thanks to the list with the same properties inside."""
    game_infos_dict = read_file(file_name, simple_string_is_enough=False)
    return game_infos_dict["genres"].count(genre)


def get_line_number_by_title(file_name, title):
    """With dictionary I could have simply use the index() method for the title and return one value higher
    to get the line number. But this can be solved with string methods also without causing error. But the
    assignment clearly instructed me to do so.
    """
    game_infos_string = read_file(file_name, simple_string_is_enough=True)
    try:
        length = game_infos_string.find(title)
        if length == -1:
            raise ValueError
    except ValueError:
        return "This title is not in the file."
    return game_infos_string[:length].count("\n") + 1


def sort_abc(file_name):
    """I have used the updated bubble sort from Python SI1"""
    game_infos_dict = read_file(file_name, simple_string_is_enough=False)
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
    game_infos_dict = read_file(file_name, simple_string_is_enough=False)
    try:
        sorted_non_redundant_genres_list = bubble_sort(list(set(game_infos_dict["genres"])))
    except TypeError:
        return "You changed the list to a non iterable type. Don't do that."
    else:
        return sorted_non_redundant_genres_list


def when_was_top_sold_fps(file_name):
    """I could use the advantage of the same types in one list solution here too. But the error handlings
    makes it harder to read.
    """
    game_infos_dict = read_file(file_name, simple_string_is_enough=False)
    top_sell = 0.0
    game_index = 0
    for index, value in enumerate(game_infos_dict["genres"]):
        if value == "First-person shooter":
            game_sold = check_conversion_error(game_infos_dict["copies sold lst"][index], index, file_name)
            if type(game_sold) == str:
                return game_sold
            elif game_sold > top_sell:
                top_sell = game_sold
                game_index = index

    year_of_top_sold_FPS = check_conversion_error(game_infos_dict["release dates"][game_index], game_index, file_name)
    return year_of_top_sold_FPS


def check_conversion_error(lst_value_str, index, file_name):
    """ I made a function instead of using two slightly different error handling"""
    outputs = {
               "copies": ["float(lst_value_str)", "second"],
               "year": ["int(lst_value_str)", "third"],
              }
    if (lst_value_str[0] in ("1", "2")) and (len(lst_value_str) == 4) and ("." not in lst_value_str):
        key = "year"
    else:
        key = "copies"
    try:
        convertable_value = eval(outputs[key][0])
    except ValueError:
        error_message = "You have letters/symbols in the " + outputs[key][1] \
                        + " value at line " + str(index + 1) + " in " + file_name
        return error_message
    else:
        return convertable_value
