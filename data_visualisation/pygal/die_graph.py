import pygal
import matplotlib.pyplot as plt
from dice import Die
from randomwalk import RandomWalk

# Pygal histogram visualisation of dice6 + dice6

die = Die(numsides=6)
die_2 = Die(numsides=6)
#die_3 = Die(numsides=6)
results = []

for x in range(5000):
    results.append(die.roll_die() + die_2.roll_die())

result_frequency = []
for frequency in range(2,max(results)+1):
    result_frequency.append(results.count(frequency))

hist = pygal.Bar()
hist.x_labels = [str(x) for x in range(2,max(results)+1)]
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6 + D6 + D6', result_frequency)
hist.render_to_file('visual_3.svg')

# Matplotlib to create a die-rolling visualisation

plt.figure(figsize=(10,6))

plt.scatter([x for x in range(2, max(results)+1)], result_frequency, s=15)
plt.xlabel('D6 + D6', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.show()

# Pygal to create a visualisation for random walk (count how many times in the same coordinate)

journey = RandomWalk(numpoints=50)
journey.fill_walk()
sorted_journey_set = sorted(set(journey.x_values))
same_coordinates_count = []

for x in sorted_journey_set:
    same_coordinates_count.append(journey.x_values.count(x))

hist = pygal.Bar()
hist.x_title = 'x coordinate'
hist.y_title = 'count'
hist.x_labels = [str(x) for x in sorted_journey_set]
hist.add('', same_coordinates_count)
hist.render_to_file('randomwalk.svg')
