# **Story Board**:

# 1. Game Theory course

### **1.1. Intro**
- Game Theory course not completed yet

### **1.2. Normal Form Games**
- N-players
- Each player has actions
- Different set of actions
- Utility function (for every player): maps an element of the cross product of all strategy spaces to the real numbers

- Rock Paper Scissors: 
    - 2 players (row player: P1, column player: P2)
    - 3 actions each
    - Utilities - 3 outcomes (P1 payoff, P2 payoff)

### **1.3. Nash Equilibrium - Pareto-Optimality**
- Given the actions of others a NE is satisfied if:
    - Each player maximises their payoff
    - Nobody has an incentive to deviate
    - If someone has an incentive to deviate the solution is not a NE
- Prisoner's Dilemma game - discuss
- Best responses 
- Looking only at Player 1's perspective
- Player 2's perspective
- The pure strategy NE: DD


- Pareto optimality concept - looks at outcomes
- Cell-1 is pareto-dominated by Cell-2 if for all players' Cell-2 >= Cell-1
- A cell is pareto-optimal if there it is not pareto-dominated by any cell
- NE is the only value that is not pareto-optimal (pareto-dominated by (3,3))
- Paradox: The Nash equilibrium is the only non-Pareto-optimal outcome 

### **1.4. Computing the Nash Equilibrium**
- Lots of methods for computing NE
- Consider 2-player game with 3 strategies
- P2: R is strictly dominated by C
- Player 2 has no reason to ever play R
- Player 1 is aware of that - can't get values of R
- P1: M is strictly dominated by U
- P2: L is strictly dominated by C
- P1: U is strictly dominated by D
- NE: DC

### **1.5. Perfect information extensive-form games**
- Another form of games - Extensive form games 
- Turn-based - Players do not play at the same time (Chess)
- Perfect information: full knowledge of history of the game
- Formulation: Tree

### **1.6. Backward Induction**
- Process of finding (subgame perfect) NE
- Starting from leaves of tree
- Work our way up the tree

### **1.7. Imperfect information extensive-form game**
- Extensive form game with partial information
- Players may be unaware of the previous players choices
- Moving on to PhD progress - questions

# 2. PhD Progress

### **2.1. Motivation - The problem**
- Ambulance service and ED interaction
- Imperfect Information Extensive form game

- Set of regulations: 95% of patients within 4 hours
- Causes ambulances blockage in an attempt to satisfy regulations
- Not necessarily a bad plan - but to what extend?

- Normally: 
    1. Ambulance arrives
    2. Patient enters hospital
    3. Depending on priority class either wait or move to treatment
- Busy day:
    1. Ambulance arrives
    2. May be blocked outside - timer never starts
    3. Ambulances remain blocked outside


### **2.2. Simulation - Markov Chain**
- Build queueing theory model to get utilities of game theoretic model 
- DES model - Markov chain model
- Parameters
- threshold: people in system s.t. block ambulances
- (u,v) - (hospital, parking)
- From state (0,0) -> ...


### **2.3. Outputs**
- Getting performance measures we need $\pi$
- Solving the following equations where ...

- Heatmap of state probabilities for larger such model
- System is mostly in states (0,2) - (0,5)

- Waiting time with $\pi$.
- Recursive formula

- Waiting times via simulation and via Markov chains model as arrivals increase


### **2.4. Future Plans**
- Interface between hospitals and ambulances
- Imperfect-Information Extensive form game:
    - Hospital 1 chooses a threshold
    - Hospital 2 chooses a threshold (unaware of H1's strategy)
    - Ambulance distributes patient to minimise their time blocked
- Objectives:
    - Hospitals: Satisfy waiting time targets
    - Ambulance: Efficiently distribute patients 

- To determine strategies of ambulance service need time blocked
- Blocking times of 2 hospitals as we vary the arrivals to them
- Point of intersection should be ambulance service strategy

- Papers:
    - Two waiting rooms
    - Game theoretic model of the EMS-ED interface