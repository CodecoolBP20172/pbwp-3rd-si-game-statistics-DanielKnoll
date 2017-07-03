

def read_file(file_name="game_stat.txt"):
    game_stats = ""
    try:
        with open(file_name) as stat:
            game_stats_string = stat.read()
    except FileNotFoundError:
        return "The game_stat.txt file is missing."
    else:
        return game_stats_string


def count_games(file_name):
    game_stats_string = read_file(file_name)
    return game_stats_string.count("\n")


def decide(file_name, year):
    game_stats_string = read_file(file_name)
    try:
        int(year)
    except ValueError as err:
        return "You should have use number: " + str(err)
    else:
        if str(year) in game_stats_string:
            return True
        else:
            return False

