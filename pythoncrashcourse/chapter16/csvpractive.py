
import csv
from matplotlib import pyplot as plt
from datetime import datetime
'''
datetime module
strptime(): interpret the date. Convert a string to a datetime format. 
			Second argument tells Python how the date is formatted.
'''
#filename='sitka_weather_07-2014.csv'
#filename='/Users/MarisolWang/Documents/GitHub/pcc/chapter_16/sitka_weather_2014.csv'
filename='/Users/MarisolWang/Documents/GitHub/pcc/chapter_16/death_valley_2014.csv'

with open(filename) as f:
	reader=csv.reader(f)
	header_row=next(reader)

	#Print headers and their positions
	#for index,column_header in enumerate(header_row):
	#	print(index,column_header)

	#Print each row of the csv reader object
	#for row in reader:
	#	print(row)
	

	'''
	Get dates, high, and low temperatures from file.

	The reader object continues from where it left off in the CSV file
	and automatically returns each line following its current position.
	next()has already read the header row,
	so the loop will begin at the second line where the actual data begins.
	'''
	dates,highs,lows=[],[],[]
	for row in reader:
		try:
			current_date=datetime.strptime(row[0],"%Y-%m-%d")
			high=int(row[1])
			low=int(row[3])
		except ValueError:
			print(current_date,'missing data')
		else:
			dates.append(current_date)
			highs.append(high)
			lows.append(low)

#plot data
fig=plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c='red',alpha=0.5) #plot the points in red
#'alpha' controls a color's transparency, alpha=0: complete transparent, alpha=1(default)is complete opaque.
plt.plot(dates,lows,c='blue',alpha=0.5)
#fill_between(): takes a series of x-values and two series of y-values and fills the space between the two y-value series.
plt.fill_between(dates, highs, lows, facecolor='blue',alpha=0.1)

#format plot
plt.title("Daily high and low temperatures - 2014\nDeath Valley, CA", fontsize=20)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate() #draws the date labels diagonally to prevent them from overlapping.
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
