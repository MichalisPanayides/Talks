"""
Code to generate plot of optimal patient distribution    
"""

import ambulance_game as abg
import matplotlib.pyplot as plt

abg.make_plot_two_hospitals_arrival_split(
    lambda_a=0.45,
    lambda_o_1=0.3,
    lambda_o_2=0.1,
    mu_1=0.05,
    mu_2=0.04,
    num_of_servers_1=12,
    num_of_servers_2=7,
    threshold_1=10,
    threshold_2=4,
    measurement_type="b",
    seed_num_1=None,
    seed_num_2=None,
    warm_up_time=100,
    trials=100,
    accuracy=20,
    runtime=10000,
)

plt.savefig("optimal_patient.png", transparent=True)
plt.close()