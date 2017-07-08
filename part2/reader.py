import sys
import datetime


def read_file(file_name, simple_string_is_enough):
    """Reader with input error handling. It can return two different type from the file
       because for some questions a simple string is enough to work with."""

    try:
        with open(file_name) as file:
            preferences_string = file.read()
    except FileNotFoundError:
        return "The game_stat.txt file is missing, or incorrect filename given."
    else:
        error = check_errors_in_file(preferences_string, file_name)
        if error != "No errors":
            sys.exit(error)

        if simple_string_is_enough:
            return preferences_string
        else:
            preferences_dict = convert_string_to_dict(preferences_string)
            return preferences_dict


def check_errors_in_file(preferences_string, file_name):
    """Input error handling. Checks if the column number per line, sold copies, release date
    is not valid. If it finds any error exits the program with a message.
    """
    preferences_lines = preferences_string.splitlines()
    for line_num, line in enumerate(preferences_lines):
        if line.count("\t") != 4:
            return "InputError: You have incorrect number of values in line " \
                   + str(line_num + 1) + " in " + file_name \
                   + "\nExpected values: title->total copies sold->release date->genre->publisher↲"

        line_lst = line.split("\t")

        for index in range(1, 3):
            converted_input = conversion_or_check_error(line_lst[index], index, line_num, file_name)
            is_error = check_value_error(converted_input, index, line_num, file_name, line_lst[0])
            if type(is_error) == str:
                return is_error

    return "No errors"


def conversion_or_check_error(value_str, index, line_num, file_name, error_check):
    """ Float and int conversion error handler in one function.
    The dictionary is to get rid of the elif case.
    """
    try:
        value_str.isdigit()
    except AttributeError:
        return "TypeError: use 'str' object"

    outputs = {
               "index == 1": ["float(value_str)", "second"],
               "index == 2": ["int(value_str)", "third"],
               "index not in (1, 2)": ["value_str"],
              }
    for key in outputs:
        if eval(key):
            try:
                converted_value = eval(outputs[key][0])
            except ValueError:
                error_message = "inputError: You have letters/symbols in the " + outputs[key][1] \
                                + " value at line " + str(line_num + 1) + " in " + file_name
                return error_message
            return converted_value


def check_value_error(value, index, line_num, file_name, title):
    """Returns error message if something is not as expected in the input file.
    It is an order dependent if-elif alternative. I had to used eval here, because some conditions
    would cause errors for different types of inputs.
    """
    keep_order = 0
    this_year = datetime.date.today().year
    value_cheks = [
            {"type(value) == str": "value"},
            {"index == 2": "3"},
            {  # This part is only for the sold copies
             "value > 500": "'InputError: You have too high second value for sold copies in line ' + " \
                            "str(line_num + 1) + ' in ' + file_name + " \
                            "'\\nAccording to Wikipedia not even Tetris reached 500M.'",

             "value < 0.1": "'InputError: Why even borher with niche games like ' + title + " \
                            "' in line ' + str(line_num + 1) + ' in ' + file_name + " \
                            "'\\nTake that line out! We are dealing with big guns here!'",
            },
            {"'No problems here'": "len(value_cheks)"},
            {  # This part is only for release dates
             "value < 1958": "'InputError: You have an earlier game release date than Pong (1958) in line ' + " \
                             "str(line_num + 1) + ' in ' + file_name",
             "value > this_year": "'InputError: You have a game which released in the future in line ' +"
                                  "str(line_num + 1) + ' in ' + file_name",

            },
            ]
    while keep_order < len(value_cheks):
        for key in value_cheks[keep_order]:
            if eval(key):
                if not value_cheks[keep_order][key].isdigit():
                    return eval(value_cheks[keep_order][key])
                keep_order = eval(value_cheks[keep_order][key])
        keep_order += 1


def convert_string_to_dict(preferences_string):
    """Puts tabulator separated columns from multiline string to a list. Stores the separate columns in dict
    with key values stored in a list to keep the same order as in the string.
    """
    preferences_dict = {}
    info_categories = ["titles", "copies sold lst", "release dates", "genres", "publishers"]
    for key in info_categories:
        preferences_dict.update({key: []})

    preferences_lines = preferences_string.splitlines()
    for line in preferences_lines:
        one_game = line.split("\t")
        for index, value in enumerate(one_game):
            convert_nums = conversion_or_check_error(value, index, line_num=None, file_name=None)
            preferences_dict[info_categories[index]].append(convert_nums)

    return preferences_dict
