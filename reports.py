

def read_file(file_name, simple_string_is_enough):
    try:
        file = open(file_name)  # I am not using with open, since I use a more complex file reading
    except FileNotFoundError:
        return "The game_stat.txt file is missing. "
    else:
        if simple_string_is_enough:
            game_stats = convert_file_to_string(file)
        else:
            game_stats = convert_file_to_dict(file)
        file.close()
        return game_stats


def convert_file_to_string(file):
    game_stats_string = file.read()
    return game_stats_string


def convert_file_to_dict(file):
    game_infos = {}
    info_category = ["title", "copies sold", "release date", "genre", "publisher"]
    for key in info_category:
        game_infos.update({key: []})

    for line in file:
        one_game = line[:-1].split("\t")
        for index, value in enumerate(one_game):
            game_infos[info_category[index]].append(value)

    return game_infos


def count_games(file_name):
    simple_string_is_enough = True
    game_stats_string = read_file(file_name, simple_string_is_enough)
    return game_stats_string.count("\n")


def decide(file_name, year):
    simple_string_is_enough = True
    game_stats_string = read_file(file_name, simple_string_is_enough)
    try:
        int(year)
    except ValueError as err:
        return "You should have use number: " + str(err)
    else:
        if str(year) in game_stats_string:
            return True
        else:
            return False
