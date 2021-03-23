import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np

import ambulance_game as abg

def get_data_of_violinplots_of_fictitious_play(
    lambda_2,
    lambda_1_1,
    lambda_1_2,
    mu_1,
    mu_2,
    num_of_servers_1,
    num_of_servers_2,
    system_capacity_1,
    system_capacity_2,
    buffer_capacity_1,
    buffer_capacity_2,
    target,
    alpha=0.5,
    iterations=100,
    seed_start=0,
    seed_reps=30,
    num_of_violiplots=8,
    use_probs=True,
):
    """
    Generate data for make_violinplots_of_fictitious_play()

    Parameters
    ----------
    lambda_2 : int
    lambda_1_1 : int
    lambda_1_2 : int
    mu_1 : int
    mu_2 : int
    num_of_servers_1 : int
    num_of_servers_2 : int
    system_capacity_1 : int
    system_capacity_2 : int
    buffer_capacity_1 : int
    buffer_capacity_2 : int
    target : int
    alpha : float, optional
    iterations : int, optional
        Number of iterations of fictitious play, by default 100
    seed_start : int, optional
        Start of the seed range, by default 0
    seed_reps : int, optional
        Seed repetitions, by default 30
    num_of_violiplots : int, optional
        The number of violin plots to be created, by default 8
    use_probs : bool, optional
        Indicator of using play probabilities (T) or play counts (F), by default True

    Returns
    -------
    numpy array
        The range of the violin plots positions
    numpy array
        numpy array containing all probabilities of row player
    numpy array
        numpy array containing all probabilities of column player
    """
    seed_range = np.linspace(seed_start, seed_start + 10000, seed_reps, dtype=int)
    violinplots_data_pos = np.linspace(1, iterations, num_of_violiplots, dtype=int)

    game = abg.game.build_game_using_payoff_matrices(
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

    all_violinplots_data_row = None
    all_violinplots_data_col = None
    for seed in seed_range:
        np.random.seed(seed)
        play_counts = tuple(game.fictitious_play(iterations=iterations))
        if use_probs:
            play_counts = [
                [
                    row_play_counts / np.sum(row_play_counts),
                    col_play_counts / np.sum(col_play_counts),
                ]
                for row_play_counts, col_play_counts in play_counts
            ]

        current_violinplot_data_row_player = None
        current_violinplot_data_col_player = None
        for pos in violinplots_data_pos:
            row_plays, col_plays = play_counts[pos]
            if (
                current_violinplot_data_row_player is None
                and current_violinplot_data_col_player is None
            ):
                current_violinplot_data_row_player = np.array([row_plays])
                current_violinplot_data_col_player = np.array([col_plays])
            else:
                current_violinplot_data_row_player = np.concatenate(
                    (current_violinplot_data_row_player, np.array([row_plays]))
                )
                current_violinplot_data_col_player = np.concatenate(
                    (current_violinplot_data_col_player, np.array([col_plays]))
                )

        if all_violinplots_data_row is None and all_violinplots_data_col is None:
            all_violinplots_data_row = [current_violinplot_data_row_player]
            all_violinplots_data_col = [current_violinplot_data_col_player]
        else:
            all_violinplots_data_row = np.concatenate(
                (
                    all_violinplots_data_row,
                    [current_violinplot_data_row_player],
                )
            )
            all_violinplots_data_col = np.concatenate(
                (
                    all_violinplots_data_col,
                    [current_violinplot_data_col_player],
                )
            )

    return violinplots_data_pos, all_violinplots_data_row, all_violinplots_data_col


def make_violinplots_of_fictitious_play(
    lambda_2,
    lambda_1_1,
    lambda_1_2,
    mu_1,
    mu_2,
    num_of_servers_1,
    num_of_servers_2,
    system_capacity_1,
    system_capacity_2,
    buffer_capacity_1,
    buffer_capacity_2,
    target,
    alpha=0.5,
    iterations=100,
    seed_start=0,
    seed_reps=30,
    num_of_violiplots=8,
    use_probs=True,
    violin_width=None,
):
    """
    Make two plots (row player, column player) of violin plots of fictitious play
    for different seeds over certain number of iterations.

    Parameters
    ----------
    lambda_2 : int
    lambda_1_1 : int
    lambda_1_2 : int
    mu_1 : int
    mu_2 : int
    num_of_servers_1 : int
    num_of_servers_2 : int
    system_capacity_1 : int
    system_capacity_2 : int
    buffer_capacity_1 : int
    buffer_capacity_2 : int
    target : int
    alpha : float, optional
    iterations : int, optional
        Number of iterations of fictitious play, by default 100
    seed_start : int, optional
        Start of the seed range, by default 0
    seed_reps : int, optional
        Seed repetitions, by default 30
    num_of_violiplots : int, optional
        The number of violin plots to be created, by default 8
    use_probs : bool, optional
        Indicator of using play probabilities (T) or play counts (F), by default True
    violin_width : float, optional
        The width of each violin plot, by default None

    Returns
    -------
    numpy array
        numpy array containing all probabilities of row player
    numpy array
        numpy array containing all probabilities of column player
    """

    (
        violinplots_data_pos,
        all_violinplots_data_row,
        all_violinplots_data_col,
    ) = get_data_of_violinplots_of_fictitious_play(
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
        iterations=iterations,
        seed_start=seed_start,
        seed_reps=seed_reps,
        num_of_violiplots=num_of_violiplots,
        use_probs=use_probs,
    )
    if violin_width is None:
        violin_width = iterations / (num_of_violiplots - 1)

    row_player_strategies = all_violinplots_data_row.shape[2]
    col_player_strategies = all_violinplots_data_col.shape[2]
    row_labels, col_labels = [], []

    plt.figure(figsize=(20, 10))
    for row_strategy in range(row_player_strategies):
        violin = plt.violinplot(
            all_violinplots_data_row[:, :, row_strategy],
            violinplots_data_pos,
            widths=violin_width,
        )
        color = violin["bodies"][0].get_facecolor().flatten()
        row_labels.append((mpatches.Patch(color=color), f"$s_{{{row_strategy + 1}}}$"))

    plt.title("Fictitious play between two hospitals (Row player)", fontsize=30)
    plt.xlabel("Iteration", fontsize=30)
    plt.ylabel("Proportion played", fontsize=30)
    plt.legend(*zip(*row_labels), fontsize=30)

    plt.figure(figsize=(20, 10))
    for col_strategy in range(col_player_strategies):
        violin = plt.violinplot(
            all_violinplots_data_col[:, :, col_strategy],
            violinplots_data_pos,
            widths=violin_width,
        )
        color = violin["bodies"][0].get_facecolor().flatten()
        col_labels.append((mpatches.Patch(color=color), f"$s_{{{col_strategy + 1}}}$"))

    plt.title("Fictitious play between two hospitals (Column player)", fontsize=30)
    plt.xlabel("Iteration", fontsize=30)
    plt.ylabel("Proportion played", fontsize=30)
    plt.legend(*zip(*col_labels), fontsize=30)

    return all_violinplots_data_row, all_violinplots_data_col


make_violinplots_of_fictitious_play(
    lambda_2=3,
    lambda_1_1=2,
    lambda_1_2=3,
    mu_1=6,
    mu_2=4,
    num_of_servers_1=1,
    num_of_servers_2=2,
    system_capacity_1=7,
    system_capacity_2=8,
    buffer_capacity_1=5,
    buffer_capacity_2=4,
    target=1,
    iterations=1000,
    seed_reps=100,
    num_of_violiplots=10,
)
plt.savefig("../fictitious_play.pdf", transparent=True)
plt.close()