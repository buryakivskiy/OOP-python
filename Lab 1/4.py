def knapsack(capasity, weights):
    F = [1] + [0]*capasity
    for i in range(len(weights)):
        for j in range(capasity, weights[i] - 1, -1):
            if F[j - weights[i]] == 1:
                F[j] = 1
    i = capasity
    while F[i] == 0:
        i -= 1
    print(i)

capasity = int(input())
weights = list(map(int, input().split()))
knapsack(capasity, weights)