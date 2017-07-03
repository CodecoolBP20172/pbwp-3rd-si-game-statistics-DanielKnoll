import reports

file_name = "game_stat.txt"
year = 2000

print("How many games are in the file?", reports.count_games(file_name))
print("Is there a game from a given year?", reports.decide(file_name, year))

file_name = "game_stat.txt" # Delete from this line before push.
is_simple_string_enough = False
t = reports.read_file(file_name, is_simple_string_enough)
print(t)
