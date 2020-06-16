"""
Script to call the real time simulation class and get
more data from it.

"""

# Imports
import sys
from BenrulesRealTimeSim import BenrulesRealTimeSim

# Main code

def main():
    # Set time step (most likely in seconds) in simulation time.
    # How long the simulation steps forward at each iteration.
    time_step = 100
    # Total number of time steps performed by the simulation.
    # Total length of simulation = time_step * number_of_steps.
    number_of_steps = 100

    # Create simulator object
    simulation = BenrulesRealTimeSim(time_step=time_step,
                                     planet_predicting='pluto',
                                     nn_path="Predict-NN-Deploy-V1.02_2-layer_relu_he-normal_msle_Adam_lr-1e-6_bs-128_epoch-3500.h5")

    # Run simulation
    curr_time_step = 0
    while curr_time_step < number_of_steps:
        curr_time_step += 1
        # Get next state of the simulation.
        current_positions, predicted_position = simulation.get_next_sim_state()

        # Output the current position of all bodies
        print("-----------------------------------------------------------------")
        for key, coordinates in current_positions.items():
            print("Name: {} / Coordinates: {}".format(key, coordinates))
        # Print predicted position
        key = list(predicted_position.keys())[0]
        print("Name: {} / Coordinates: {}".format(key,
                                                  predicted_position.get(key)))
        print("-----------------------------------------------------------------")
    return None

if __name__ == "__main__":
    main()
    sys.exit()