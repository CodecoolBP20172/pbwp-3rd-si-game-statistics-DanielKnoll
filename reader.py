import sys
import datetime


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
            sys.exit(error)

        if simple_string_is_enough:
            game_infos = convert_file_to_string(file)
        else:
            game_infos = convert_file_to_dict(file)
        file.close()
        return game_infos


def check_errors_in_file(file, file_name):
    """Input error handling. First I check if the lines contains less/more values.
    Then I check if the sold copies is a number or not, or has unrealistic value.
    Then I check if the year is a number, or valid year, or from the past or from the future.
    Title, genre, publisher can be whatever. Although I could add a txt file with genres and check
    if the input is from those.
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
    """ I made a function instead of using two slightly different error handling"""
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
    """For the first two questions for example f I can simply return a string to work with."""
    game_infos_string = file.read()
    return game_infos_string


def convert_file_to_dict(file):
    """For the most of the questions the program will create a dictionary for each function call.
    Instead of doing the obvious and storing the file line by line in lists I figured I can use
    simple commands if I store the columns in separate lists. I used the property names as keys
    so it will be easier to read the code.
    Since the information categories are in the same order as in the file I could append the right
    value to the right dictionary key. The game informations will be in the same indexes but in
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
