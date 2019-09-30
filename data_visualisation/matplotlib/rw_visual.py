import matplotlib.pyplot as plt
from randomwalk import RandomWalk


while True:
    rw_visual = RandomWalk()
    rw_visual.fill_walk()
    point_numbers = list(range(rw_visual.numpoints))

    # c=point_numbers: gradient from first position to ending position
    plt.figure(figsize=(10,6))
    plt.scatter(rw_visual.x_values, rw_visual.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=10)
    plt.scatter(rw_visual.x_values[0], rw_visual.y_values[0], c='green', s=10)
    plt.scatter(rw_visual.x_values[-1], rw_visual.y_values[-1], c='red', s=10)

    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    user_input = input('Do you want to make another plot? y/n ')
    if user_input.lower() == 'n':
        break
