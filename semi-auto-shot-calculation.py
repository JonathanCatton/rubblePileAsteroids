import math
import matplotlib.pyplot as plt
import numpy as np

hit_percentage_list = np.linspace(0,120,120)
semi_auto_shots = [3]
full_auto_shots = [5]
print(semi_auto_shots)
single_shot_expectation_value = []
semi_auto_expectation_value = []
shots_fired = 0

for hit_chance in hit_percentage_list:
    single_shot_expectation_value.append((hit_chance+10)/100)

plt.plot(hit_percentage_list,single_shot_expectation_value, label='Single Shot')

for num_shots in semi_auto_shots:
    semi_auto_expectation_value = []
    for hit_chance in hit_percentage_list:
        shots_fired = 1
        sum_expectation = 0
        while hit_chance > 0 and shots_fired <= num_shots:
            if hit_chance < 10 or shots_fired == num_shots:
                sum_expectation += hit_chance*shots_fired/100
            else:
                sum_expectation += 10*shots_fired/100
            hit_chance -= 10
            shots_fired += 1
        semi_auto_expectation_value.append(sum_expectation)
    plt.plot(hit_percentage_list,semi_auto_expectation_value, label='Semi-Auto Fire (' + str(num_shots) + ') shots')


for num_shots in full_auto_shots:
    full_auto_expectation_value = []
    for hit_chance in hit_percentage_list:
        hit_chance -= 10
        shots_fired = 1
        sum_expectation = 0
        while hit_chance > 0 and shots_fired <= num_shots:
            if hit_chance < 10 or shots_fired == num_shots:
                sum_expectation += hit_chance*shots_fired/100
            else:
                sum_expectation += 10*shots_fired/100
            hit_chance -= 10
            shots_fired += 1
        full_auto_expectation_value.append(sum_expectation)
    plt.plot(hit_percentage_list,full_auto_expectation_value, label='Full-Auto Fire (' + str(num_shots) + ') shots')

plt.xlabel('Target Number Before Shot Choice')
plt.ylabel('Expectation Value Of Hits')
plt.legend()
plt.show()
