import matplotlib.pyplot as plt
import numpy as np

def display_matches(teams):
    """
    Display the matches to be played for the tournament.
    """
    play_order = ((0, 1), (2, 3), (1, 2), (0, 3), (1, 3), (0, 2))
    print(f"{teams[play_order[0][0]]} \t VS \t {teams[play_order[0][1]]}")
    print(f"{teams[play_order[1][0]]} \t VS \t {teams[play_order[1][1]]}")
    print(f"{teams[play_order[2][0]]} \t VS \t {teams[play_order[2][1]]}")
    print(f"{teams[play_order[3][0]]} \t VS \t {teams[play_order[3][1]]}")
    print(f"{teams[play_order[4][0]]} \t VS \t {teams[play_order[4][1]]}")
    print(f"{teams[play_order[5][0]]} \t VS \t {teams[play_order[5][1]]}")


def get_match_results(match):
    """
    Get the results of one match. That is, the scores of each player at each
    round. Two lists are returned, (one for each player) containing the scores
    of each round.
    """
    A = np.array([
        [3, 0],
        [5, 1],
    ])
    B = np.array([
        [3, 5],
        [0, 1],
    ])
    row_player_scores = []
    col_player_scores = []

    for roundd in match:
        choice_a = ord(roundd[0]) - 67
        choice_b = ord(roundd[1]) - 67

        row_player_scores.append(A[choice_a][choice_b])
        col_player_scores.append(B[choice_a][choice_b])

    return row_player_scores, col_player_scores


def display_outcomes(teams, matches):
    """
    Display the results of the matches played and print the scores of each
    player for each match.
    """
    game_1, game_2, game_3, game_4, game_5, game_6 = matches

    all_scores_1 = []
    all_scores_2 = []
    all_scores_3 = []
    all_scores_4 = []
    
    if game_1[0] == "":
        print(f"Match 1: {teams[0]} VS {teams[1]}")
        print("\tTBD", end="\n\n")
    else:
        result_1 = get_match_results(game_1)
        print(f"Match 1: {teams[0]} VS {teams[1]}")
        print(f" RESULT: {sum(result_1[0])} - {sum(result_1[1])}", end="\n\n")
        all_scores_1 = all_scores_1 + result_1[0]
        all_scores_2 = all_scores_2 + result_1[1]

    if game_2[0] == "":
        print(f"Match 2: {teams[2]} VS {teams[3]}")
        print("\tTBD", end="\n\n")
    else:
        result_2 = get_match_results(game_2)
        print(f"Match 2: {teams[2]} VS {teams[3]}")
        print(f" RESULT: {sum(result_2[0])} - {sum(result_2[1])}", end="\n\n")
        all_scores_3 = all_scores_3 + result_2[0]
        all_scores_4 = all_scores_4 + result_2[1]

    if game_3[0] == "":
        print(f"Match 3: {teams[1]} VS {teams[2]}")
        print("\tTBD", end="\n\n")
    else:
        result_3 = get_match_results(game_3)
        print(f"Match 3: {teams[1]} VS {teams[2]}")
        print(f" RESULT: {sum(result_3[0])} - {sum(result_3[1])}", end="\n\n")
        all_scores_2 = all_scores_2 + result_3[0]
        all_scores_3 = all_scores_3 + result_3[1]
    
    if game_4[0] == "":
        print(f"Match 4: {teams[0]} VS {teams[3]}")
        print("\tTBD", end="\n\n")
    else:
        result_4 = get_match_results(game_4)
        print(f"Match 4: {teams[0]} VS {teams[3]}")
        print(f" RESULT: {sum(result_4[0])} - {sum(result_4[1])}", end="\n\n")
        all_scores_1 = all_scores_1 + result_4[0]
        all_scores_4 = all_scores_4 + result_4[1]

    if game_5[0] == "":
        print(f"Match 5: {teams[1]} VS {teams[3]}")
        print("\tTBD", end="\n\n")
    else:
        result_5 = get_match_results(game_5)
        print(f"Match 5: {teams[1]} VS {teams[3]}")
        print(f" RESULT: {sum(result_5[0])} - {sum(result_5[1])}", end="\n\n")
        all_scores_2 = all_scores_2 + result_5[0]
        all_scores_4 = all_scores_4 + result_5[1]

    if game_6[0] == "":
        print(f"Match 6: {teams[0]} VS {teams[2]}")
        print("\tTBD", end="\n\n")
    else:
        result_6 = get_match_results(game_6)
        print(f"Match 6: {teams[0]} VS {teams[2]}")
        print(f" RESULT: {sum(result_6[0])} - {sum(result_6[1])}", end="\n\n\n")
        all_scores_1 = all_scores_1 + result_6[0]
        all_scores_3 = all_scores_3 + result_6[1]

    print(f"{teams[0]}:\t {np.sum(all_scores_1)}")
    print(f"{teams[1]}:\t {np.sum(all_scores_2)}")
    print(f"{teams[2]}:\t {np.sum(all_scores_3)}")
    print(f"{teams[3]}:\t {np.sum(all_scores_4)}")

    return all_scores_1, all_scores_2, all_scores_3, all_scores_4


def plot_gameplay(team_scores, teams):
    """
    Plot the cumulative scores of each team over the course of the tournament.
    """
    plt.figure(figsize=(13, 6))
    plt.plot([i for i in range(len(team_scores[0]))], np.cumsum(team_scores[0]))
    plt.plot([i for i in range(len(team_scores[1]))], np.cumsum(team_scores[1]))
    plt.plot([i for i in range(len(team_scores[2]))], np.cumsum(team_scores[2]))
    plt.plot([i for i in range(len(team_scores[3]))], np.cumsum(team_scores[3]))
    plt.xlabel("Time (Rounds)")
    plt.ylabel("Score")
    plt.legend(teams)
    plt.show();


def plot_cooperate_ratio(matches, teams):
    """
    Plot the ratio of cooperation to defection for each team over the course of the tournament.
    """
    if (np.array(matches) == "").any():
        return "Not all matches have been played yet."

    match_1, match_2, match_3, match_4, match_5, match_6 = matches
    
    play_order = ((0, 1), (2, 3), (1, 2), (0, 3), (1, 3), (0, 2))

    responses_1 = [term[0] for term in match_1] + [term[0] for term in match_4] + [term[0] for term in match_6]
    responses_2 = [term[1] for term in match_1] + [term[0] for term in match_3] + [term[0] for term in match_5]
    responses_3 = [term[0] for term in match_2] + [term[1] for term in match_3] + [term[1] for term in match_6]
    responses_4 = [term[1] for term in match_2] + [term[1] for term in match_4] + [term[1] for term in match_5]

    c_responses = [team.count("C") / 15 * 100 for team in [responses_1, responses_2, responses_3, responses_4]]
    d_responses = [team.count("D") / 15 * 100 for team in [responses_1, responses_2, responses_3, responses_4]]

    plt.figure(figsize=(16, 8))
    plt.bar(teams, c_responses, bottom=d_responses, width=0.5, color="green", label="Cooperate")
    plt.bar(teams, d_responses, width=0.5, color="red", label="Defect")
    plt.legend(loc=10, fontsize=12)
    plt.xlabel("Teams", fontsize=16)
    plt.ylabel("Cooperate/Defect Ratio (%)", fontsize=16)
    plt.show();