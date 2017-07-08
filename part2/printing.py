
import sys
import pprint
import reports


def input_values():
    file_name = "game_stat.txt"
    title = "The Sims 3"
    return file_name, title


def print_get_most_played(file_name):
    question = "What is the title of the most played game?"
    answer = reports.get_most_played(file_name)
    my_pretty_print(question, answer)


def print_sum_sold(file_name):
    question = "How many copies have been sold total?"
    answer = reports.sum_sold(file_name)
    my_pretty_print(question, answer)


def print_get_selling_avg(file_name):
    question = "What is the average selling?"
    answer = reports.get_selling_avg(file_name)
    my_pretty_print(question, answer)


def print_count_longest_title(file_name):
    question = "How many characters long is the longest title?"
    answer = reports.count_longest_title(file_name)
    my_pretty_print(question, answer)


def print_get_date_avg(file_name):
    question = "What is the average of the release dates?"
    answer = reports.get_date_avg(file_name)
    my_pretty_print(question, answer)


def print_get_game(file_name, title):
    question = "What properties has a game?"
    answer = reports.get_game(file_name, title)
    my_pretty_print(question, answer)


def print_count_grouped_by_genre(file_name):
    question = "How many games are there grouped by genre?"
    answer = reports.count_grouped_by_genre(file_name)
    my_pretty_print(question, answer)


def print_get_date_ordered(file_name):
    question = "What is the date ordered list of the games?"
    answer = reports.get_date_ordered(file_name)
    my_pretty_print(question, answer)


def my_pretty_print(question, answer):
    """Formated output. Prints a different answer output according the type of the answer"""
    answer_printers = {
        "type(answer) == list and len(str(answer)) < 80": "print()\n" + "pprint.pprint(answer, indent=40, width=55)",
        "type(answer) == list and len(str(answer)) > 80": "print()\n" + "pprint.pprint(answer, indent=35, width=90)",
        "type(answer) == bool": "print('{:36}{}'.format(' ', answer))",
        "type(answer) == dict": "print()\n" + "pprint_sorted_dict(answer, 35)",
        "type(answer) == float": "print(' {:^75.3f}'.format(answer))",
        "type(answer) not in (list, bool, dict, float)": "print(' {:^75}'.format(answer))",
        }
    print("-"*85+"\nQuestion:{:^75}\nAnswer:".format(question), end="")
    for key in answer_printers:
        if eval(key):
            exec(answer_printers[key])


def pprint_sorted_dict(_dict, indent=0):
    """Returns a sorted dictionary like pprint, but pprint can't have key=str.lower"""
    if indent == 0:
        end = ""
    elif indent > 0 or len(str(_dict)) > 80:
        end = "\n"
    sorted_keys = sorted([i for i in _dict], key=str.lower)
    print("{" + " "*(indent-1) + "'" + sorted_keys[0] + "'" + ": " + str(_dict[sorted_keys[0]]) + ",", end=end)
    for index in range(1, len(sorted_keys) - 1):
        print(" "*indent + "'" + sorted_keys[index] + "'" + ": " + str(_dict[sorted_keys[index]]) + ",", end=end)
    print(" "*indent + "'" + sorted_keys[-1] + "'" + ": " + str(_dict[sorted_keys[-1]]) + "}")


def main():
    file_name, title = input_values()
    print_get_most_played(file_name)
    print_sum_sold(file_name)
    print_get_selling_avg(file_name)
    print_count_longest_title(file_name)
    print_get_date_avg(file_name)
    print_get_game(file_name, title)
    print_count_grouped_by_genre(file_name)
    print_get_date_ordered(file_name)

if __name__ == '__main__':
    sys.exit(main())
