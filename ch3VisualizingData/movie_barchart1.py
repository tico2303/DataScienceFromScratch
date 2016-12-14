import matplotlib.pyplot as plt 

movies = ["Spotlight", "Mad Max", "The Revenant", "Birdman", "Whiplash"]
num_awards = [2, 6, 3, 4, 3]

#bars are by default a width of 0.8, so we add 0.1 to the left coordinates 
# so that earch bar is centered
lxc = [i+0.1 for i,_ in enumerate(movies)]

#plot bars with left x-coordinates [lxc], heights [num_awards]
plt.bar(lxc, num_awards)

plt.ylabel("# of Awards")
plt.title("Movies")

#labeling x-axis with movie names at bar centers
plt.xticks( [i+0.5 for i,_ in enumerate(movies)], movies)
plt.show()
