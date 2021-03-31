
import csv

from matplotlib import pyplot as plt
from datetime import datetime

filename='sitka_weather_07-2014.csv'
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
	Get dates and high temperatures from file.

	The reader object continues from where it left off in the CSV file
	and automatically returns each line following its current position.
	next()has already read the header row,
	so the loop will begin at the second line where the actual data begins.
	'''
	dates,highs=[],[]
	for row in reader:
		current_date=datetime.strptime(row[0],"%Y-%m-%d")
		dates.append(current_date)

		high=int(row[1])
		highs.append(high)

#plot data
fig=plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c='red')

#format plot
plt.title("Daily high temperatures, July 2014", fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

#comment
