import matplotlib.pyplot as plt

mentions = [500,505]
years = [2013, 2014]

plt.bar( [x - 0.4 for x in years],mentions, 0.8)

#sets the interval marks on the x-axis
plt.xticks(years)

plt.ylabel("# of times I heard 'Data Science'")
plt.xlabel("Year")

plt.ticklabel_format(useOffset=False)
plt.axis([2012.5, 2014.5, 0,500])

plt.show()

