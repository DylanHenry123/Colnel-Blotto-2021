file = open("strategies_two.txt", "w")
permutations_for_three = [[3, 3, 0],
                          [3, 0, 3],
                          [0, 3, 3],
                          [4, 1, 1],
                          [1, 4, 1],
                          [1, 1, 4],
                          [2, 2, 2],
                          [3, 2, 1],
                          [3, 1, 2],
                          [2, 3, 1],
                          [2, 1, 3],
                          [1, 3, 2],
                          [1, 2, 3],
                          [4, 2, 0],
                          [4, 0, 2],
                          [2, 4, 0],
                          [2, 0, 4],
                          [0, 2, 4],
                          [0, 4, 2],
                          [5, 1, 0],
                          [5, 0, 1],
                          [1, 0, 5],
                          [1, 5, 0],
                          [0, 5, 1],
                          [0, 1, 5],
                          [0, 0, 6],
                          [0, 6, 0],
                          [6, 0, 0]]

for i in range(len(permutations_for_three)):
    for j in range(len(permutations_for_three)):
        file.write(f"{permutations_for_three[i][0]}, {permutations_for_three[i][1]}, {permutations_for_three[i][2]}/{permutations_for_three[j][0]}, {permutations_for_three[j][1]}, {permutations_for_three[j][2]}\n")

