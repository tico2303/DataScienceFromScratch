from __future__ import print_function
import matplotlib.pyplot as plt

variance = [ 2**x for x in range(9)]
print("variance:     ", variance)

bias_squared = [ 2**x for x in range(8,-1, -1)]
print("bias_squared: ", bias_squared)

# recall: zip takes an element from each list and creates a 
#          tuple of them
total_error = [x + y for x,y in zip(variance, bias_squared)]

xs = [i for i, _ in enumerate(variance)]

# we can make multiple calls to plt.plot
# to show multiple series on the same chart
plt.plot(xs, variance,    'g-', label='variance')     #green solid line
plt.plot(xs, bias_squared,'r-.', label='bias^2')      #red dot-dashed line
plt.plot(xs, total_error, 'b:',  label='total error') #blue dotted line

# because we assigned labels to each series 
# we can get a legend for free
# loc=9 means "top center"
plt.legend(loc=9)
plt.xlabel("model complexity")
plt.title("Bias-Variance TradeOff")
plt.show()


