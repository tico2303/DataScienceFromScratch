from __future__ import print_function
import matplotlib.pyplot as plt

friends = [70,65,72,63,71,64,60,64,67]
minutes = [175,170,205,120,220,130,105,145,190]

# labels are letters from 'a' to 'j'
labels = [chr(a) for a in range(97,107)]

plt.scatter(friends, minutes)

#print(zip(labels, friends, minutes))

#label each point
for label, friend_count, minute_count in zip(labels, friends, minutes):
    #plt.annotate will place a label at the given xy coordinates
    plt.annotate(label,
                xy=(friend_count, minute_count), #put the label with its point
                xytext=(5,-5),                   #but slightly offset
                textcoords='offset points')


plt.title("Daily Minutes Vs. Number of friends")
plt.show()


