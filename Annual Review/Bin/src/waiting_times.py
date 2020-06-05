"""
Code to generate waiting times    
"""

import ambulance_game as abg
import matplotlib.pyplot as plt

plt.figure(figsize=(20, 10))
abg.get_plot_comparing_times(
    lambda_a=0.2,
    lambda_o=0.1,
    mu=0.2,
    num_of_servers=5,
    threshold=6,
    system_capacity=20,
    parking_capacity=20,
    runtime=10000,
    num_of_trials=10,
    seed_num=0,
    output="ambulance",
    plot_over="lambda_o",
    max_parameter_value=1,
    accuracy=10
)

plt.savefig("waiting_times.png", transparent=True)
plt.close()