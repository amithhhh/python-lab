
players = {
    "Virat Kohli": 765,
    "Rohit Sharma": 597,
    "Quinton de Kock": 594,
    "Daryl Mitchell": 552,
    "Rachin Ravindra": 578,
    "Kane Williamson": 332,
    "David Warner": 535,
    "Travis Head": 329
}


sorted_players = dict(sorted(players.items(), key=lambda x: x[1], reverse=True))

print("Players sorted by total scores (descending):")
for name, score in sorted_players.items():
    print(name, ":", score)
