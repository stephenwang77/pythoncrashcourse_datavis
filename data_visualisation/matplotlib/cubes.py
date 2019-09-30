import matplotlib.pyplot as plt

"""Data visualisation of cubed values from 0-5000 and colour mapped"""

x_values = [x for x in range(1,5001)]
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=15)
plt.xlabel('values', fontsize=12)
plt.ylabel('cubed values', fontsize=12)
plt.title('cubes', fontsize=14)
plt.savefig('cubes.png', bbox_inches='tight')
