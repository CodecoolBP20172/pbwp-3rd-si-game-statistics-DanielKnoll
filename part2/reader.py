import sys
import datetime


def read_file(file_name, simple_string_is_enough):
    """Reader with input error handling. It can return two different type from the file"""
    try:
        file = open(file_name)
    except FileNotFoundError:
        return "The game_stat.txt file is missing, or incorrect filename given."
    else:
        error = check_errors_in_file(file, file_name)
        if error != "No errors":
            sys.exit(error)

        if simple_string_is_enough:
            game_infos = convert_file_to_string(file)
        else:
            game_infos = convert_file_to_dict(file)
        file.close()
        return game_infos


def check_errors_in_file(file, file_name):
    """Input error handling. Checks if the colunm number per line, sold copies, release date
    is not valid. If it finds any error exits the program with a message.
    """
    for line_num, line in enumerate(file):
        if line.count("\t") != 4:
            return "InputError: You have incorrect number of values in line " \
                   + str(line_num) + " in " + file_name \
                   + "\nExpected values: title->total copies sold->release date->genre->publisher↲"

        current_line = line[:-1].split("\t")

        converted_sold_copy = check_conversion_error(current_line[1], line_num, file_name)
        if type(converted_sold_copy) == str:
            return converted_sold_copy
        elif converted_sold_copy > 500:
            return "InputError: You have too high second value for sold copies in line " \
                   + str(line_num + 1) + " in " + file_name \
                   + "\nAccording to Wikipedia not even Tetris reached 500M."
        elif converted_sold_copy < 0.1:
            return "InputError: Why even borher with niche games like " \
                   + current_line[0] + " in line " + str(line_num + 1) + " in " + file_name \
                   + "\nTake that line out! We are dealing with big guns here!"

        converted_release_date = check_conversion_error(current_line[2], line_num, file_name)
        if type(converted_release_date) == str:
            return converted_release_date
        elif (len(str(converted_release_date)) != 4) or (str(converted_release_date)[0] not in ("1", "2") or (
              converted_release_date < 0)):
            return "InputError: You have a number at the third value in line " \
                   + str(line_num + 1) + " in " + file_name \
                   + "which is not a valid year."
        elif converted_release_date < 1958:
            return "InputError: You have an earlier game release date than Pong (1958) in line " \
                   + str(line_num + 1) + " in " + file_name
        elif converted_release_date > datetime.date.today().year:
            return "InputError: You have a game which released in the future in line " \
                   + str(line_num + 1) + " in " + file_name

    file.seek(0)
    return "No errors"


def check_conversion_error(lst_value_str, line_num, file_name):
    """ Float and int convertion error handler in one function."""
    outputs = {
               "copies": ["float(lst_value_str)", "second"],
               "year": ["int(lst_value_str)", "third"],
              }
    if (lst_value_str[0] in ("1", "2")) and (len(lst_value_str) >= 4) and ("." not in lst_value_str):
        key = "year"
    else:
        key = "copies"
    try:
        convertable_value = eval(outputs[key][0])
    except ValueError:
        error_message = "You have letters/symbols in the " + outputs[key][1] \
                        + " value at line " + str(line_num + 1) + " in " + file_name
        return error_message
    else:
        return convertable_value


def convert_file_to_string(file):
    """For some questions a simple string is enough to work with."""
    game_infos_string = file.read()
    return game_infos_string


def convert_file_to_dict(file):
    """Returns a dictionary with same properties in one list. Information about a single
    game will be stored in the same list index under different keys.
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
