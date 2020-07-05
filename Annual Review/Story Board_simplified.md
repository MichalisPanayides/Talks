# **Story Board**:

# 2.PhD Progress

### **2.1. Motivation - The problem**
- Ambulance service and ED interaction
- Game Theoretic scenario informed by queueing theoretic models

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
- Illustrate examples of the two models that were used
- DES model - Markov chain model (DESCRIBE)
- Parameters
- threshold: people in system s.t. block ambulances
- (u,v) - (hospital, parking)
- From state (0,0) -> ...


### **2.3. Outputs**
- Getting performance measures we need $\pi$
- Solving the following equations where ...

- Heatmap of state probabilities for larger such model
- System is mostly in states (0,2) - (0,5)

- Mean Waiting time of either ambulance or other patients
- Overall Waiting Time

- Waiting times via simulation and via Markov chains model as arrivals increase


### **2.4. Future Plans**
- Need to arrive at 2 matrices for the 2 hospital game
- Utility is a number based on how well the regulations are satisfied 

- To determine strategies of ambulance service need time blocked
- Blocking times of 2 hospitals as we vary the arrivals
- Point of intersection should be the strategy of the ambulance service

- Interface between hospitals and ambulances
- Imperfect-Information Extensive form game:
    - Hospital 1 chooses a threshold
    - Hospital 2 chooses a threshold (unaware of H1's strategy)
    - Ambulance distributes patient to minimise their time blocked
- Objectives:
    - Hospitals: Satisfy waiting time targets
    - Ambulance: Efficiently distribute patients 