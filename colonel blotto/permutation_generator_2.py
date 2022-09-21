soldiers = 3
permutations = []

for i in range(soldiers):
    for j in range(soldiers):
        for k in range(soldiers):
            if i + j + k == soldiers:
                permutations.append([i, j, k])

file = open("strategies.txt", "w")

for i in range(len(permutations)):
    file.write(str(permutations[i]))
