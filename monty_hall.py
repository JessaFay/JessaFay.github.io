# monty_hall.py

import random


class Simulation:
    """
    class Simulation for the Monty Hall Problem - Numberphile.
    """

    def __init__(self, doornum):
        """
        Initialize Simulation for object.

        Parameters:
        - doornum (int): The number of door options used to play the game.
        """
        self.numdoors = doornum

    def set_random_doors(self):
        """
        Create a list containing 'zonk' strings and replace one item with 'car' different all three times selected at random.

        Returns:
        - list: The list representing doors with one containing 'car' and others 'zonk'.
        """
        doors = ['zonk'] * self.numdoors
        car_index = random.randint(0, self.numdoors - 1)
        doors[car_index] = 'car'
        return doors

    def choose_doors(self):
        """
        Choose the first selected door for the Player and another door as an alternate option; both doors selected randomly.

        Returns:
        - tuple: The player door and the alternate door.
        """
        doors = self.set_random_doors()

        # Ensure that the player chooses a door
        player_door = random.choice(doors)

        # Monty opens one of the Zonk doors
        zonk_doors = [door for door in doors if door != 'car' and door != player_door]

        # Check if there are Zonk doors available
        if zonk_doors:
            monty_opens = random.choice(zonk_doors)

            # Monty opens the chosen door
            doors.remove(monty_opens)

            # The remaining door is the alternate door
            alternate_door = doors[0]

            return player_door, alternate_door

        # If there are no Zonk doors, retry the process
        return self.choose_doors()

    def play_game(self, switch=False, iterations=1):
        """
        Simulate the player playing the Monty Hall game, by iterations.

        Parameters:
        - switch (bool): Whether the contestant switches doors. Default is False.
        - iterations (int): The number of times the game will be played. Default is 1.

        Returns:
        - float: Percentage of times the game ended with a win.
        """
        wins = 0
        for _ in range(iterations):
            player_door, alternate_door = self.choose_doors()

            # If switching doors option is True
            if switch:
                player_door = alternate_door

            # Check if the player wins
            if player_door == 'car':
                wins += 1

        win_percentage = wins / iterations if iterations > 0 else 0
        return win_percentage


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

