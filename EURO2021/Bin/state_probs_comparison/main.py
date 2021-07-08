import matplotlib.pyplot as plt
import numpy as np

import ambulance_game as abg

lambda_1 = 1
lambda_2 = 1
mu = 1
num_of_servers = 3
threshold = 2
system_capacity = 4
buffer_capacity = 2

all_states = abg.markov.build_states(
    threshold=threshold,
    system_capacity=system_capacity,
    buffer_capacity=buffer_capacity,
)
transition_matrix = abg.markov.get_transition_matrix(
    lambda_2=lambda_2,
    lambda_1=lambda_1,
    mu=mu,
    num_of_servers=num_of_servers,
    threshold=threshold,
    system_capacity=system_capacity,
    buffer_capacity=buffer_capacity,
)
pi = abg.markov.get_steady_state_algebraically(
    Q=transition_matrix, algebraic_function=np.linalg.lstsq
)

sim_state_probabilities_array = (
    abg.simulation.get_average_simulated_state_probabilities(
        lambda_2=lambda_2,
        lambda_1=lambda_1,
        mu=mu,
        num_of_servers=num_of_servers,
        threshold=threshold,
        system_capacity=system_capacity,
        buffer_capacity=buffer_capacity,
        seed_num=0,
        runtime=2000,
        num_of_trials=10,
        output=np.ndarray,
    )
)
markov_state_probabilities_array = abg.markov.get_markov_state_probabilities(
    pi=pi,
    all_states=all_states,
    output=np.ndarray,
    system_capacity=system_capacity,
    buffer_capacity=buffer_capacity,
)
diff_states_probabilities_array = (
    sim_state_probabilities_array - markov_state_probabilities_array
)

plt.figure(figsize=(6, 4))
plt.imshow(sim_state_probabilities_array, cmap="Blues")
for i in range(sim_state_probabilities_array.shape[0]):
    for j in range(sim_state_probabilities_array.shape[1]):
        if not np.isnan(sim_state_probabilities_array[i, j]):
            plt.text(
                j,
                i,
                "{:.2f}".format(sim_state_probabilities_array[i, j]),
                ha="center",
                va="center",
                color="chocolate",
                fontsize=15,
            )
plt.title("Simulation", fontsize=11, fontweight="bold")
plt.yticks([0, 1, 2])
plt.xlabel("Queue 2", fontsize=11, fontweight="bold")
plt.ylabel("Queue 1", fontsize=11, fontweight="bold")
plt.colorbar()
plt.savefig("simulation.png", transparent=True)


plt.figure(figsize=(6, 4))
plt.imshow(markov_state_probabilities_array, cmap="Blues")
for i in range(markov_state_probabilities_array.shape[0]):
    for j in range(markov_state_probabilities_array.shape[1]):
        if not np.isnan(markov_state_probabilities_array[i, j]):
            plt.text(
                j,
                i,
                "{:.2f}".format(markov_state_probabilities_array[i, j]),
                ha="center",
                va="center",
                color="chocolate",
                fontsize=15,
            )
plt.title("Markov chain", fontsize=11, fontweight="bold")
plt.yticks([0, 1, 2])
plt.xlabel("Queue 2", fontsize=11, fontweight="bold")
plt.ylabel("Queue 1", fontsize=11, fontweight="bold")
plt.colorbar()
plt.savefig("markov.png", transparent=True)


plt.figure(figsize=(6, 4))
plt.imshow(diff_states_probabilities_array, cmap="Blues")
for i in range(diff_states_probabilities_array.shape[0]):
    for j in range(diff_states_probabilities_array.shape[1]):
        if not np.isnan(diff_states_probabilities_array[i, j]):
            plt.text(
                j,
                i,
                "{:.0e}".format(diff_states_probabilities_array[i, j]),
                ha="center",
                va="center",
                color="chocolate",
                fontsize=14,
            )
plt.title("Differences", fontsize=11, fontweight="bold")
plt.yticks([0, 1, 2])
plt.xlabel("Queue 2", fontsize=11, fontweight="bold")
plt.ylabel("Queue 1", fontsize=11, fontweight="bold")
plt.colorbar()
plt.savefig("diff.png", transparent=True)
