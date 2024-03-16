Time = 40817772
Distance = 219101213651089

possible_wins = []
for push in range(0, Time):
    max_distance = (Time - push) * push
    if max_distance > Distance:
        possible_wins.append(max_distance)

print(str(len(possible_wins)))