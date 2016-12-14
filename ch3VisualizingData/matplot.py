from __future__ import print_function
import matplotlib.pyplot as plt

years = [x for x in range(1950,2011,10)]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6,10289.7, 14958.3]

#years x-axis, gdp y-axis
plt.plot(years, gdp, color='red', marker='x', linestyle='solid')

#title
plt.title("Nominal GDP")

#labeling x, y axis 
plt.ylabel("Billions of $")
plt.xlabel("Year")
plt.show()