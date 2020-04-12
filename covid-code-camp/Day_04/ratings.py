bands = ("MercyMe", "Count Basie Orchestra", "Coldplay", "REO Speedwagon", 
"The Association", "The Police", "The Bee Gees", "Steve Green", "Manheim Steamroller", "Abba")

bandRatings = {}

for band in bands: 
	print ("Rate " + band + ". (1-10)")
        rating = input(":")
    # add rating and band to dictionary
        bandRatings.update({band: int(rating)})

totalRatings = 0
numRatings = 0

print("\nYour Ratings:")
for band, rating in bandRatings.items():
	print(band + ":  " + str(rating))
        totalRatings = totalRatings + rating
       	numRatings = numRatings + 1

average = totalRatings / numRatings 

print("\nYour average rating is a: " + str(average))
