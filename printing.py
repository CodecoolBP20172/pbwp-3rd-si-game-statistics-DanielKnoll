import sys
import pprint
import reports


def input_values():
    file_name = "game_stat.txt"
    year = 2000
    genre = "First-person shooter"
    title = "The Sims 2"
    return file_name, year, genre, title


def print_count_games(file_name):
    question = "How many games are in the file?"
    answer = reports.count_games(file_name)
    my_pretty_print(question, answer, type(answer))


def print_decide(file_name, year):
    question = "Is there a game from year {}?".format(year)
    answer = reports.decide(file_name, year)
    my_pretty_print(question, answer, type(answer))


def print_get_latest(file_name):
    question = "Which was the latest game?"
    answer = reports.get_latest(file_name)
    my_pretty_print(question, answer, type(answer))


def print_count_by_genre(file_name, genre):
    question = "How many {} games do we have?".format(genre)
    answer = reports.count_by_genre(file_name, genre)
    my_pretty_print(question, answer, type(answer))


def print_get_line_number_by_title(file_name, title):
    question = "What is the line number of {}?".format(title)
    answer = reports.get_line_number_by_title(file_name, title)
    my_pretty_print(question, answer, type(answer))


def print_sort_abc(file_name):
    question = "What is the alphabetical ordered list of the titles?"
    answer = reports.sort_abc(file_name)
    my_pretty_print(question, answer, type(answer))


def print_get_genres(file_name):
    question = "What are the genres?"
    answer = reports.get_genres(file_name)
    my_pretty_print(question, answer, type(answer))


def print_when_was_top_sold_fps(file_name):
    question = "What is the release date of the top sold 'First-person shooter' game?"
    answer = reports.when_was_top_sold_fps(file_name)
    my_pretty_print(question, answer, type(answer))


def my_pretty_print(question, answer, answer_type):
    """Formated output. Prints a different answer output according the type of the answer"""
    answer_printers = {
                    list: ["print()", "pprint.pprint(answer, indent=36)"],
                    bool: ["print('{:36}{}'.format(' ', answer))"],
                    "else": ["print(' {:^75}'.format(answer))"],
                    }
    print("-"*85+"\nQuestion:{:^75}\nAnswer:".format(question), end="")
    if answer_type not in (list, bool):
        answer_type = "else"
    for command in answer_printers[answer_type]:
        eval(command)


def main():
    file_name, year, genre, title = input_values()
    print_count_games(file_name)
    print_decide(file_name, year)
    print_get_latest(file_name)
    print_count_by_genre(file_name, genre)
    print_get_line_number_by_title(file_name, title)
    print_sort_abc(file_name)
    print_get_genres(file_name)
    print_when_was_top_sold_fps(file_name)

if __name__ == '__main__':
    sys.exit(main())
