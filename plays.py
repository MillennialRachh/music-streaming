songs = ["Bad and Boujee", "Megatron", "No Scrubs", "What's Going On", "Respect", "Sky Walker"]
playcounts = [78, 29, 44, 21, 89, 5]

song_counts = zip(songs, playcounts)

plays = {key:value for key, value in zip(songs, playcounts)}

print(plays)

plays["Purple Haze"] = 1

plays["Respect"] = 94

library = {"The Best Songs": plays, "Sunday Feelings": {}}

print(library)
