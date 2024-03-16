input_file = open('input.txt', 'r')
all_lines = input_file.readlines()

game_power = []
sum = 0

for line in all_lines:
    game_number = line.strip().split(":")[0].split()[1]
    games = line.strip().split(":")[1].strip().split(";")
    greens = 0
    blues = 0
    reds = 0
    for game in games:
        balls = game.strip().split(",")
        for ball in balls:
            ball = ball.strip().split()
            ball_colour = ball[1].strip()
            ball_number = int(ball[0].strip())
            if ball_colour == "red" and ball_number > reds:
                reds = ball_number
            if ball_colour == "blue" and ball_number > blues:
                blues = ball_number
            if ball_colour == "green" and ball_number > greens:
                greens = ball_number
    game_power.append(reds * blues * greens)

print(game_power)
print(str(len(game_power)))

for power in game_power:
    sum = sum + power
print(str(sum))
