def water_jug_problem():
    j1 = 0
    j2 = 0
    cj1 = 7  
    cj2 = 5  
    goal = 3

    steps = []

    while True:
        if len(steps)> 30:
            steps.append("No solution found.")
            break

        if j1 == goal or j2 == goal:
            steps.append(f"Goal reached: ({j1}, {j2})")
            break

        if j1 == 0:
           j1 = cj1
           steps.append(f"Fill jug1: ({j1}, {j2})")

        elif j2 < cj2:
             pour = min(j1, cj2 - j2)
             j1 -= pour
             j2 += pour
             steps.append(f"Pour jug1 to jug2: ({j1}, {j2})")

        elif j2 == cj2:
             j2 = 0
             steps.append(f"Empty jug2: ({j1}, {j2})")

    return steps


result = water_jug_problem()
for step in result:
    print(step)