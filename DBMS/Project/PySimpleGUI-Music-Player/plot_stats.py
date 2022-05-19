import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('album_data.csv','r') as csvfile:
	plots = csv.reader(csvfile, delimiter = ',')
	
	for row in plots:
		x.append(row[0])
		y.append(int(row[1]))

plt.bar(x, y, color = 'g', width = 0.72, label = "Frequency")
plt.xlabel('Time')
plt.ylabel('Ages')
plt.title('Music quality')
plt.legend()
plt.show()
