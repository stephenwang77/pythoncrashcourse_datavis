import matplotlib.pyplot as plt
from randomwalk import RandomWalk

molecular_path = RandomWalk()
molecular_path.fill_walk()

plt.figure(figsize=(10,6))
plt.plot(molecular_path.x_values, molecular_path.y_values, linewidth=1)
plt.scatter(molecular_path.x_values[0], molecular_path.y_values[0], c='green', s=15)
plt.scatter(molecular_path.x_values[-1], molecular_path.y_values[-1], c='red', s=15)
plt.show()
