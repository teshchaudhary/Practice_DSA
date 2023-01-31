def winner(arr):
    d = {}
    for i in arr:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    winner = max(sorted(d), key=d.get)  # Lexicographically Smaller
    maxVotes = max(d.values())

    return (winner, maxVotes)
