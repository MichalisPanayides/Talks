import matplotlib.pyplot as plt
import numpy as np

import ambulance_game as abg

lambda_2 = 2

lambda_1_1 = 1
mu_1 = 1
num_of_servers_1 = 3
threshold_1 = 3
system_capacity_1 = 4
buffer_capacity_1 = 4

lambda_1_2 = 1
mu_2 = 1
num_of_servers_2 = 3
threshold_2 = 2
system_capacity_2 = 4
buffer_capacity_2 = 4

hospital_1_times = tuple()
hospital_2_times = tuple()

prop_1_range = np.linspace(0, 1, 20)

for prop_1 in prop_1_range:

    lambda_2_1 = prop_1 * lambda_2
    lambda_2_2 = (1 - prop_1) * lambda_2

    mean_blocking_time_1 = (
        abg.markov.get_mean_blocking_time_using_markov_state_probabilities(
            lambda_2=lambda_2_1,
            lambda_1=lambda_1_1,
            mu=mu_1,
            num_of_servers=num_of_servers_1,
            threshold=threshold_1,
            system_capacity=system_capacity_1,
            buffer_capacity=buffer_capacity_1,
        )
    )

    mean_blocking_time_2 = (
        abg.markov.get_mean_blocking_time_using_markov_state_probabilities(
            lambda_2=lambda_2_2,
            lambda_1=lambda_1_2,
            mu=mu_2,
            num_of_servers=num_of_servers_2,
            threshold=threshold_2,
            system_capacity=system_capacity_2,
            buffer_capacity=buffer_capacity_2,
        )
    )

    hospital_1_times += (mean_blocking_time_1,)
    hospital_2_times += (mean_blocking_time_2,)

plt.figure(figsize=(9, 5))
plt.plot(prop_1_range, hospital_1_times)
plt.plot(prop_1_range, hospital_2_times)

plt.title("Blocking times over different values of $p_A$ $(T_A = 3, T_B = 2)$")
plt.xlabel("$p_A$")
plt.ylabel("Blocking time")

plt.legend(["Hospital A", "Hospital B"])
plt.savefig("main.png", transparent=True)
