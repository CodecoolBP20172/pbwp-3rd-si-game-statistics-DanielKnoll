import sys
import reports


def input_values():
    file_name = "game_stat.txt"
    year = 2000
    genre = "First-person shooter"
    title = "The Sims 2"
    return file_name, year, genre, title


def get_answers(inputs):
    """Returns a single string for the file exporter"""
    answers = (str(reports.count_games(inputs[0])) + "\n" +
               str(reports.decide(inputs[0], inputs[1])) + "\n" +
               reports.get_latest(inputs[0]) + "\n" +
               str(reports.count_by_genre(inputs[0], inputs[2])) + "\n" +
               str(reports.get_line_number_by_title(inputs[0], inputs[3])) + "\n" +
               ", ".join(reports.sort_abc(inputs[0])) + "\n" +
               ", ".join(reports.get_genres(inputs[0])) + "\n" +
               str(reports.when_was_top_sold_fps(inputs[0])) + "\n")
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
