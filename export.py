import sys
import reports


def input_values():
    file_name = "game_stat.txt"
    year = 2000
    genre = "First-person shooter"
    title = "The Sims 2"
    return file_name, year, genre, title


def get_answers(inputs):
    file_name, year, genre, title = inputs
    """Returns a single string for the file exporter"""
    answers = (str(reports.count_games(file_name)) + "\n" +
               str(reports.decide(file_name, year)) + "\n" +
               reports.get_latest(file_name) + "\n" +
               str(reports.count_by_genre(file_name, genre)) + "\n" +
               str(reports.get_line_number_by_title(file_name, title)) + "\n" +
               ", ".join(reports.sort_abc(file_name)) + "\n" +
               ", ".join(reports.get_genres(file_name)) + "\n" +
               str(reports.when_was_top_sold_fps(file_name)) + "\n")
    return answers


def export_answers(answers):
    with open("export_answers.txt", "w") as f:
        is_it_done = f.write(answers)
    if is_it_done > 0:
        print("You can find your answers in export_answers.txt")


def main():
    inputs = input_values()
    answers = get_answers(inputs)
    export_answers(answers)

if __name__ == '__main__':
    sys.exit(main())
