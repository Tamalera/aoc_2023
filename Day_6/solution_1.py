Time = [40, 81, 77, 72]
Distance = [219, 1012, 1365, 1089]

races = {}
for d in range(0, len(Distance)):
    races[d] = []
for idx, t in enumerate(Time):
    for push in range(0, t):
        max_distance = (t - push) * push
        if max_distance > Distance[idx]:
            races[idx].append(max_distance)
res = 1
for race in races:
    res = res * len(races[race])

print(str(res))