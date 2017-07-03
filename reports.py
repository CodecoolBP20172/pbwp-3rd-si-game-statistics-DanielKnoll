

def read_file(file_name, simple_string_is_enough):
    """In the first version it was a file reading using with open, but I found out that some
    functions can return the correct value from a simple string. So I made two separate reader.
    One returns a string the other returns a dictionary. In order to do that I had to keep open
    the file until the return command.
    """
    try:
        file = open(file_name)
    except FileNotFoundError:
        return "The game_stat.txt file is missing, or incorrect filename given."
    else:
        if simple_string_is_enough:
            game_infos = convert_file_to_string(file)
        else:
            game_infos = convert_file_to_dict(file)
        file.close()
        return game_infos


def convert_file_to_string(file):
    """For example for the first two questions I can simply return a string to work with."""
    game_infos_string = file.read()
    return game_infos_string


def convert_file_to_dict(file):
    """For the most of the questions the program will create a dictionary for each function call.
    I did this to avoid global variables.
    The game information categories will be the keys. Each category receives an empty list
    through a for loop. The game informations will be appended to the corresponding dict keys.
    The game will have it's information in the same indexes but in different lists.
    I got rid of the \n with a slice command at the end of each line, and split the line at tabulators.
    Since the information categories are in the same order as in the file I could append the right value to
    the right dictionary key.
    This will make easier to work with the same type of data, and reading the code.
    """

    game_infos = {}
    info_categories = ["title", "copies sold", "release date", "genre", "publisher"]
    for key in info_categories:
        game_infos.update({key: []})

    for line in file:
        one_game = line[:-1].split("\t")
        for index, value in enumerate(one_game):
            game_infos[info_categories[index]].append(value)

    return game_infos


def count_games(file_name):
    """I can simply count the games by counting the EOL characters (\n) in the string since each game
    is in a separate line. With different data structure the function has to be changed. But this way 
    it uses less resources.
    """
    simple_string_is_enough = True
    game_infos_string = read_file(file_name, simple_string_is_enough)
    return game_infos_string.count("\n")


def decide(file_name, year):
    """Another simple string operation, but I added a value check for the new argument."""
    simple_string_is_enough = True
    game_infos_string = read_file(file_name, simple_string_is_enough)
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
    a different list ({"title": [?,?,?,...]}) but at the same index.
    I could have use a one-liner but it would have made the code harder to read.
    """
    simple_string_is_enough = False
    game_infos_dict = read_file(file_name, simple_string_is_enough)
    latest_year = max(game_infos_dict["release date"])
    index = game_infos_dict["release date"].index(latest_year)
    return game_infos_dict["title"][index]


def count_by_genre(file_name, genre):
    """Here I could use a simple list count thanks to the list with the same categories of values inside."""
    simple_string_is_enough = False
    game_infos_dict = read_file(file_name, simple_string_is_enough)
    return game_infos_dict["genre"].count(genre)


def get_line_number_by_title(file_name, title):
    """With dictionary I could have simply use the .index method for the title and return one value higher
    to get the line number. But this can be solved with string methods also.
    """
    simple_string_is_enough = True
    game_infos_string = read_file(file_name, simple_string_is_enough)
    length = game_infos_string.find(title)
    return game_infos_string[:length].count("\n") + 1
