import sys
import reports


def input_values():
    file_name = "game_stat.txt"
    title = "The Sims 2"
    return file_name, title


def get_answers(inputs):
    """Returns a single string for the file exporter"""
    file_name, title = inputs
    answers = (reports.get_most_played(file_name) + "\n" +
               str(reports.sum_sold(file_name)) + "\n" +
               str(reports.get_selling_avg(file_name)) + "\n" +
               str(reports.count_longest_title(file_name)) + "\n" +
               str(reports.get_date_avg(file_name)) + "\n" +
               str(reports.get_game(file_name, title)) + "\n" +
               str(reports.count_grouped_by_genre(file_name)) + "\n" +
               str(reports.get_date_ordered(file_name)) + "\n")
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
