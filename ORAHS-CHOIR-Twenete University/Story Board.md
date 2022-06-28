# **Story Board**:


## 1. Intro
- About me
- My PhD - queueing model + game model

## 2. Motivation
- Ambulances wait for a long time outside of hospitals (blocked)
  - Good: Patients have their own paramedic
  - Bad: Ambulances blocked - can't get more patients
- From patient's perspective two queues (one outside + one inside)
- NHS: regulations - patients need to be seen within 4 hours
- Hospital's strategy: Delay the timer

## 3. Markov chain formulation
- My network
  - Structure
  - Parameters
- Markov chain (untruncated):
  - Two queues - states: (u, v)
  - Threshold
  - Rates
- Markov chain (truncated):
  - To be able to solve it
  - Markov chain VS Diagrammatic representation

## 4. Generator matrix - Steady state - Performance measures
- Generator matrix
- Steady state probabilities
- Blocking time
- Proportion of individuals within target

## 5. Game
- Game
  - 2 Hospitals + 1 Ambulance
  - Distribute patients to hospitals
  - Objectives:
    - p_A -> Minimise time blocked
    - T -> Satisfy the NHS regulations

## 6. Game Theoretic model
- Game:
  - Players
  - Strategies
  - Objectives
- Game - Formulation
  - Imperfect information extensive form game
- Hospital's utility
  - Can be anything
  - For different values of T_A, T_B
  - Proportion close to 95%
- Payoff matrices:
  - Utility for every value of T_A and T_B
  - Routing matrix: p_A

## 7. Learning Algorithms
- Asymmetric Replicator Dynamics:
  - Learning algorithm
  - Used to express the evolutionary dynamics of an entity
  - Example:
    - Large population of some agents (replicators)
    - Different types of agents meet
    - Meeting (interaction of different replicators) generates payoffs -> fitness
  - Game theory: replicators are strategies
- Results: Base run
  - Consider a game between two hospitals
    - Hospital capacities: 6, 7
    - Thresholds from 0 to (6, 7)
  - Hospitals stable at T = 5, 6
  - Inefficiencies stabilised
  - **Punch line**
- Results: Applying incentives
  - Same game as before
  - Incentives change outcome
  - Inefficiencies go even lower
  - **Punch line**

## 8. Reinforcement Learning
- Last thing we thought interesting - RL
- Use just the queueing model
- Servers choose their service rate based on maximising some utility function
- Assume:
  - Four servers (custom priority)
  - Choose rates s.t
  - Maximise (Idle time) + (Lost inds) -- (can be anything)
- PLOTS:
  - LEFT: Utilities over time
  - RIGHT: Server rates over time
  - At some point flood system and then fix it
  - Interesting:
    - Servers try to handle the demand but cannot
    - Servers remember their rates

## 9. Picture slide
- Thank you