# Story Board

## Introduction
- Interaction between EMS and ED - why ambulances blocked - picture
- NHS regulations: patients to be seen within 4 hours
- Busy day - hospital may block ambulances to satisfy regulations
    - No enter -> No timer
    - Not necessarily a bad plan - ?? But to what extend ??
- 3-player game (AMBULANCE + 2 HOSPITALS)
    - Hospitals objective: Satisfy time targets
    - Ambulance objective: Minimise the time blocked
- Inform game - a queueing model

## Queueing model (Upper right)
- DES version model
- Two arrival rates ...
- To model blockages
    - Patient at parking
    - Stay there until hospital chooses otherwise
    - Strategies of the game

## Markov chain (Lower left)
- Markov chain version of queueing model
    - horizontal-axis: number of people in hospital
    - vertical-axis: number of people in parking
- Connection to figure above
- Strategy = Threshold of 2
    - (0,2) from 1-dimensional to 2-dimensional
    - Which is when we start blocking

## Game (Lower right)
- 3-player game:
    - Hospital 1 chooses a threshold (unaware of H2's strategy)
    - Hospital 2 chooses a threshold (unaware of H1's strategy)
    - Ambulance Service chooses how to distribute ambulances (aware of all strategies)
- Example of playing the game using fictitious play (perspective of one hospital):
    - Proportion of strategies played over time
    - Strategies converge to a threshold of 5
    - 1 example of behaviour that emerges
- All work done in parallel with ethnography - used to validate model
