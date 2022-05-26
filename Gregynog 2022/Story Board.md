# **Story Board**:


## 1. Intro
- About me

## 2. Queues examples
- Queue 1 server
  - Components
  - Parameters
  - Markovian/Markovian/1 server
  - Markov chain: states, comparison with queue
- Queue 3 server
  - Single queue + 3 servers
  - Markovian/Markovian/3 servers
  - Markov chain: μ, 2μ, 3μ, 3μ 

## 3. Markov chain formulation
- Ambulances queueing outside of the hospital
  - From patient's perspective two queues (one outside + one inside)
  - NHS: regulations - patients need to be seen within 4 hours
  - Hospital's strategy: Delay the timer
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
- State probabilities - performance measures

## 5. Performance Measures for custom queue
- Game
  - 2 Hospitals + 1 Ambulance
  - Distribute patients to hospitals
  - Objectives:
    - p_A -> Minimise time blocked
    - T -> Satisfy the NHS regulations
- Performance measures overview
  - Not too much detail
- Game: Objectives

## 6. Game Theoretic model
- Game:
  - Players
  - Strategies
- Game - Formulation
  - Imperfect information extensive form game
- Hospital's utility
  - Can be anything
  - For different values of T_A, T_B
  - Proportion close to 95%
- Payoff matrices:
  - Utility for every value of T_A and T_B
  - Routing matrix: p_A

## 8. Learning Algorithms
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

## 10. Picture slide
- Thank you