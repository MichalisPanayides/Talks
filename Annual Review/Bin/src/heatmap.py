"""
Code to generate heatmaps
"""
import matplotlib.pyplot as plt
import ambulance_game as abg

plt.figure(figsize=(20, 10))
abg.get_heatmaps(
    lambda_a=0.1,
    lambda_o=0.3,
    mu=0.1,
    num_of_servers=5,
    threshold=5,
    system_capacity=20,
    parking_capacity=20,
    runtime=10000,
    num_of_trials=10,
    seed_num=0,
)

plt.savefig("heatmap.png", transparent=True)
plt.close()
