input_file = open('input.txt', 'r')
all_lines = input_file.readlines()

max_red = 12
max_green = 13
max_blue = 14

sum = 0


def is_possible_game(game) -> bool:
    for single_round in game:
        balls = single_round.strip().split(",")
        for ball in balls:
            if ball.split()[1] == "red" and int(ball.split()[0]) > max_red:
                return False
            if ball.split()[1] == "blue" and int(ball.split()[0]) > max_blue:
                return False
            if ball.split()[1] == "green" and int(ball.split()[0]) > max_green:
                return False
    return True


for line in all_lines:
    game_number = line.strip().split(":")[0].split()[1]
    games = line.strip().split(":")[1].strip().split(";")
    if is_possible_game(games):
        sum = sum + int(game_number)

print(str(sum))
