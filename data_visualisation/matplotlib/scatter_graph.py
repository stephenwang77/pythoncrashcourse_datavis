import matplotlib.pyplot as plt

input_values = [x for x in range(51)]
squares = [x**2 for x in input_values]

# Scatter plot and label axes
plt.scatter(input_values, squares, c=input_values, cmap=plt.cm.Blues, edgecolor='none', s=15)
plt.title('scatter squares', fontsize=16)
plt.xlabel('value', fontsize=8)
plt.ylabel('squared value', fontsize=8)

# axis function(min_x, max_x, min_y, max_y) specifies range of x and y axis
plt.axis([0,60,0,3000])

plt.tick_params(axis='both',labelsize=6)

plt.show()
