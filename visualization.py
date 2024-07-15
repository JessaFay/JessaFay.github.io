# visualization.py

import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import monty_hall

class Plot:
    """
    Plot class for visualizing the Monty Hall simulation results.
    """

    def __init__(self, doors=3, iterations=200):
        """
        Initialize Plot object.

        Parameters:
        - doors (int): The number of doors for the simulation, default is set at 3.
        - iterations (int): The number of iterations made in the simulation, default is set at 200.
        """
        self.doors = doors
        self.iterations = iterations
        self.sequence = []

    def make_plot(self):
        """
        Generate a visualization of how many times the player wins.
        """
        for i in range(1, self.iterations + 1):
            switch = i % 2 == 0
            simulation_instance = monty_hall.Simulation(doornum=self.doors)
            win_percentage = simulation_instance.play_game(switch=switch, iterations=i)
            self.sequence.append({
                'iterations': i,
                'percentage': win_percentage,
                'doors': self.doors,
                'switched': str(switch),
            })

        df = pd.DataFrame(self.sequence)
        sns.lineplot(data=df, x='iterations', y='percentage', hue='switched')
        plt.title(f"Monty Hall Simulation ({self.doors} doors)")
        plt.xlabel("Number of Times Played")
        plt.ylabel("Win Percentage")
        plt.show()

if __name__ == "__main__":
    # Test the Plot class to get results
    plot_instance = Plot(doors=3, iterations=400)
    plot_instance.make_plot()





