import matplotlib.pyplot as plt

input_values = [x for x in range(1,6)]
squares = [x**2 for x in range(1,6)]

# Chart table and label axes
plt.plot(input_values, squares, linewidth=5)
plt.title('squares', fontsize=16)
plt.xlabel('value', fontsize=12)
plt.ylabel('square of value', fontsize=12)

# Set size of tick labels
plt.tick_params(axis='both', labelsize=6)

plt.show()
