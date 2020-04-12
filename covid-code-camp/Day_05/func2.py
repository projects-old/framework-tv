def battingAverage(atBats, hits, walks):
	average = float(hits) / (atBats - walks)
	return average
    	#print("Batting Average: %4.3f" % (average))

def sluggingAverage(totalBases = 1, atBats = 1):
	sluggingAverage = float(totalBases) / atBats
	return sluggingAverage
        #print("Slugging Average: %4.3f" % (sluggingAverage))

atBats = input("At Bats: ")
totalBases = input("Total Bases: ")
hits = input("Hits: ")
walks = input("Walks: ")

ba = battingAverage(atBats, hits, walks)
sa = sluggingAverage(totalBases, atBats)

#avg = battingAverage(520, 174, 29)

print("The batting average is %4.3f and the slugging average is %4.3f." % (ba, sa))
