import sys
import pprint
import reports


def input_values():
    file_name = "game_stat.txt"
    year = 2000
    genre = "First-person shooter"
    title = "The Sims 2"
    return file_name, year, genre, title


def get_QA_count_games(file_name):
    return "How many games are in the file?", reports.count_games(file_name)


def get_QA_decide(file_name, year):
    return "Is there a game from year {}?".format(year), reports.decide(file_name, year)


def get_QA_get_latest(file_name):
    return "Which was the latest game?", reports.get_latest(file_name)


def get_QA_count_by_genre(file_name, genre):
    return "How many {} games do we have?".format(genre), reports.count_by_genre(file_name, genre)


def get_QA_get_line_number_by_title(file_name, title):
    return "What is the line number of {}?".format(title), reports.get_line_number_by_title(file_name, title)


def get_QA_sort_abc(file_name):
    return "What is the alphabetical ordered list of the titles?", reports.sort_abc(file_name)


def get_QA_get_genres(file_name):
    return "What are the genres?", reports.get_genres(file_name)


def get_QA_when_was_top_sold_fps(file_name):
    return ("What is the release date of the top sold 'First-person shooter' game?",
            reports.when_was_top_sold_fps(file_name))


def pretty_it_up(func):
    print("-"*70+"\nQuestion:{:^60}".format(func[0]))
    if type(func[1]) == list:
        print("Answer:")
        pprint.pprint(func[1], indent=30)
    elif type(func[1]) == bool:
        print("{:36}{}".format("Answer:", func[1]))
    else:
        print("Answer: {:^60}".format(func[1]))


def main():
    inputs = input_values()
    pretty_it_up(get_QA_count_games(inputs[0]))
    pretty_it_up(get_QA_decide(inputs[0], inputs[1]))
    pretty_it_up(get_QA_get_latest(inputs[0]))
    pretty_it_up(get_QA_count_by_genre(inputs[0], inputs[2]))
    pretty_it_up(get_QA_get_line_number_by_title(inputs[0], inputs[3]))
    pretty_it_up(get_QA_sort_abc(inputs[0]))
    pretty_it_up(get_QA_get_genres(inputs[0]))
    pretty_it_up(get_QA_when_was_top_sold_fps(inputs[0]))

if __name__ == '__main__':
    sys.exit(main())
