n = int(input())
games = list(map(int,input().strip().split()))
minscore = games[0]
maxscore = games[0]
hscore = 0
lscore = 0
for i in range(1,len(games)):
	if games[i] < minscore:
		minscore = games[i]
		lscore += 1
	elif games[i] > maxscore:
		maxscore = games[i]
		hscore += 1
	else:
		pass
print(hscore,lscore)


