import matplotlib.pyplot as plt
import nashpy as nash
import numpy as np

import ambulance_game as abg

lambda_2 = 2
alpha = 0
target = 3.11

lambda_1_1 = 1
mu_1 = 1
num_of_servers_1 = 3
system_capacity_1 = 4
buffer_capacity_1 = 4

lambda_1_2 = 1
mu_2 = 1
num_of_servers_2 = 3
system_capacity_2 = 4
buffer_capacity_2 = 4

A, B, R = abg.game.get_payoff_matrices(
    lambda_2=lambda_2,
    lambda_1_1=lambda_1_1,
    lambda_1_2=lambda_1_2,
    mu_1=mu_1,
    mu_2=mu_2,
    num_of_servers_1=num_of_servers_1,
    num_of_servers_2=num_of_servers_2,
    system_capacity_1=system_capacity_1,
    system_capacity_2=system_capacity_2,
    buffer_capacity_1=buffer_capacity_1,
    buffer_capacity_2=buffer_capacity_2,
    target=target,
    alpha=alpha,
)
A += 1
B += 1

print("R = ", R)
print("A = ", A)
print("B = ", B)
print("")
print("Corrected A = \n", np.round(100000 * (A - 0.9999), 2))
print("Corrected B = \n", np.round(100000 * (B - 0.9999), 2))

game = nash.Game(A, B)
print("N.E. = ", tuple(game.support_enumeration()))
