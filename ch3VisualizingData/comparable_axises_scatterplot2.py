from __future__ import print_function
import matplotlib.pyplot as plt

test_1_grades = [99, 90, 85, 97, 80]
test_2_grades = [100, 85, 60, 90, 70]

plt.scatter(test_1_grades, test_2_grades)
#plt.title("Axes Are NOT Comparable")
plt.xlabel("test 1 grades")
plt.ylabel("test 2 grades")
#plt.show()

# the inequality in the axis is fixed using
plt.title("Axes ARE Comparable")
plt.axis("equal")
plt.show()
